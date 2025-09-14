# import mysql.connector as sql
# import pandas as pd
# import json

# # Connect to MySQL
# connection = sql.connect(
#     host='3.111.252.210',
#     database='kmb_extraction',
#     user='root',
#     password='AlgoTeam123'
# )

# # duplicate detection query
# report_query = """
#     SELECT
#         o.case_id,
#         o.customer_name,
#         o.crn,
#         o.created_date,
#         CASE
#             WHEN COUNT(*) OVER (PARTITION BY o.customer_name, o.crn, DATE(o.created_date)) > 1
#             THEN 'DUPLICATE'
#             ELSE 'UNIQUE'
#         END AS duplicate_case
#     FROM kmb_extraction.ocr o
#     WHERE o.customer_name IS NOT NULL
#       AND o.crn IS NOT NULL
# """

# flag=True

# #Use pandas.read_sql with the connection
# df = pd.read_sql(report_query, connection)

# # Normalize column names
# df.columns = df.columns.str.lower()

# # Remove duplicate columns if any
# df = df.loc[:, ~df.columns.duplicated()]
# response_data=
#   {
#     message="All Duplicate"
#     data=json.loads(df)
#     flag=True
#   }

#   return response_data



from flask import Flask, jsonify
import mysql.connector as sql
import pandas as pd

app = Flask(__name__)

# MySQL connection details
db_config = {
    "host": "3.111.252.210",
    "database": "kmb_extraction",
    "user": "root",
    "password": "AlgoTeam123"
}

@app.route("/duplicates", methods=["GET"])
def get_duplicates():
    try:
        # Connect to MySQL
        connection = sql.connect(**db_config)

        # SQL Query
        report_query = """
            SELECT
                o.case_id,
                o.customer_name,
                o.crn,
                o.created_date,
                CASE
                    WHEN COUNT(*) OVER (PARTITION BY o.customer_name, o.crn, DATE(o.created_date)) > 1
                    THEN 'DUPLICATE'
                    ELSE 'UNIQUE'
                END AS duplicate_case
            FROM kmb_extraction.ocr o
            WHERE o.customer_name IS NOT NULL
              AND o.crn IS NOT NULL
        """

        # Fetch data into Pandas
        df = pd.read_sql(report_query, connection)
        df.columns = df.columns.str.lower()
        df = df.loc[:, ~df.columns.duplicated()]

        # Prepare response
        response_data = {
            "message": "All Duplicate",
            "data": df.to_dict(orient="records"),
            "flag": True
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"message": "Error", "error": str(e), "flag": False}), 500

if __name__ == "__main__":
    result=app.run(debug=True, host="0.0.0.0", port=5000)
    print(result)


