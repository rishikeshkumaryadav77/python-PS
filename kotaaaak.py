import mysql.connector as sql
import pandas as pd
from mysql.connector import Error
connection = sql.connect(host='3.111.252.210',
                        # database='kmb_queues',
                        user='root',
                        password='AlgoTeam123')
print(connection)
cursor = connection.cursor()
 
 
 
# query = f'SELECT `file_name` FROM `process_queue` LEFT JOIN `ocr_info` ON `process_queue.case_id` = `ocr_info.case_id`  limit 20'
# query1 = f'SELECT `case_id` FROM `ocr_info`'
# query2 = f'desc `process_queue` '
# query_desc_process = f'DESCRIBE `process_queue`'
# query_desc_ocr = f'DESCRIBE `ocr_info`'
query3 = """SELECT * FROM kmb_queues.process_queue LEFT JOIN kmb_queues.ocr_info ON ocr_info.case_id = process_queue.case_id """
data = pd.read_sql(query3, connection)
print(data)