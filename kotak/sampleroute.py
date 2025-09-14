def reconciliation_report():
    logging.info('Calling Reconciliation Report')
    try:
        memory_before = measure_memory_usage()
        start_time = tt()
    except Exception:
        logging.warning("Failed to start RAM/time tracking")
 
    try:
        data = request.json
        tenant_id = data['ui_data']['tenant_id']
        start_date = data['start_date']
        end_date = data['end_date']
        db_config['tenant_id'] = tenant_id
 
        trace_id = generate_random_64bit_string()
        attr = ZipkinAttrs(
            trace_id=trace_id,
            span_id=generate_random_64bit_string(),
            parent_span_id=None,
            flags=None,
            is_sampled=False,
            tenant_id=tenant_id
        )
 
        with zipkin_span(
            service_name='reports_api',
            zipkin_attrs=attr,
            span_name='reconciliation_report',
            transport_handler=http_transport,
            sample_rate=0.5
        ):
            hdfc_db = DB('queues', **db_config)
 
            report_query = f"""
                SELECT
                    NVL(TO_CHAR(pq.case_id), '') AS case_id,
                    NVL(TO_CHAR(fd.party_id), '') AS party_id,
                    NVL(TO_CHAR(pq.hub_code), '') AS hub_code,
                    NVL(TO_CHAR(pq.branch_code), '') AS branch_code,
                    NVL(TO_CHAR(pq.branch_name), '') AS branch_name,
                    NVL(TO_CHAR(ocr.party_name), '') AS party_name,
                    NVL(fd.initial_file_name, '') AS initial_file_name,
                    NVL(fd.final_file_name, '') AS final_file_name,
                    NVL(TO_CHAR(fd.merged_file_count), '') AS merged_file_count,
                    NVL(TO_CHAR(fd.file_received_datetime, 'YYYY-MM-DD HH24:MI:SS'), '') AS file_received_datetime,
                    NVL(TO_CHAR(pq.last_updated, 'YYYY-MM-DD HH24:MI:SS.FF'), '') AS last_updated,
                    NVL(TO_CHAR(pq.created_date, 'YYYY-MM-DD HH24:MI:SS'), '') AS created_date,
                    NVL(pq.status, '') AS status
                FROM hdfc_queues.file_data fd
                JOIN hdfc_extraction.ocr ocr ON fd.party_id = ocr.party_id
                JOIN hdfc_queues.process_queue pq ON fd.final_file_name = pq.file_name
                WHERE fd.FILE_RECEIVED_DATETIME BETWEEN
                      TO_TIMESTAMP('{start_date}', 'YYYY-MM-DD HH24:MI:SS')
                  AND TO_TIMESTAMP('{end_date}', 'YYYY-MM-DD HH24:MI:SS')
                ORDER BY fd.FILE_RECEIVED_DATETIME DESC
            """
 
            df = hdfc_db.execute_(report_query)
            df.columns = df.columns.str.lower()
 
            df = df.loc[:, ~df.columns.duplicated()]
            df = df.drop_duplicates(subset=['initial_file_name'])
 
            outputs = []
            serial_number = 1
            for _, row in df.iterrows():
                output = {
                    'serial_number': serial_number,
                    'case_id': row.get('case_id', ''),
                    'party_id': row.get('party_id', ''),
                    'hub_code':row.get('hub_code',''),
                    'branch_code':row.get('branch_code',''),
                    'branch_name':row.get('branch_name',''),
                    'party_name': row.get('party_name', ''),
                    'initial_file_name': row.get('initial_file_name', ''),
                    'final_file_name': row.get('final_file_name', ''),
                    'merged_file_count': row.get('merged_file_count', ''),
                    'file_received_datetime': row.get('file_received_datetime', ''),
                    'last_updated': row.get('last_updated', ''),
                    'created_date': row.get('created_date', ''),
                    'status': row.get('status', '')
                }
 
                # Convert datetime fields to string
                for key in ['file_received_datetime', 'last_updated', 'created_date']:
                    if output[key]:
                        output[key] = str(output[key])
 
                outputs.append(output)
                serial_number += 1
 
            # Save Excel file
            ist = pytz.timezone("Asia/Calcutta")
            timestamp = datetime.now(ist).strftime("%m-%d-%Y_%H_%M")
            filename = f'Reconciliation_Report--{timestamp}.xlsx'
            path = f'/var/www/reports_api/reports/{filename}'
 
            try:
                pd.DataFrame(outputs).to_excel(path, index=False)
            except Exception as e:
                logging.exception(f"Excel export failed: {e}")
 
            # Build the return JSON
            return_json_data = {
                'message': 'SUCCESS',
                'excel_flag': 1,
                'flag': True,
                'data': [{'row_data': outputs}]
            }
 
            # Optional: useful for template rendering
            data['report_data'] = return_json_data
 
    except Exception as e:
        logging.exception(f"Error generating reconciliation report: {e}")
        return jsonify({'flag': False, 'message': 'Failed to generate reconciliation report'})
 
    try:
        memory_after = measure_memory_usage()
        memory_consumed = (memory_after - memory_before) / (1024 * 1024 * 1024)
        end_time = tt()
        logging.info(f"Memory Used: {memory_consumed:.10f} GB | Time: {round(end_time - start_time, 3)} s")
    except Exception:
        logging.warning("Memory/time tracking failed")
 
    return jsonify(return_json_data)
