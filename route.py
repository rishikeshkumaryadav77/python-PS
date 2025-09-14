import mysql.connector as sql
import pandas as pd
from mysql.connector import Error
connection = sql.connect(host='3.111.252.210',
                        database='kmb_extraction',
                        user='root',
                        password='AlgoTeam123')
print(connection)
cursor = connection.cursor()
 
# query1 = """
# SELECT
#     ocr.customer_name,
#     ocr.crn,
#     ocr.created_date,
#     CASE
#         WHEN COUNT(*) OVER (PARTITION BY customer_name, crn, DATE(created_date)) > 1
#         THEN 'DUPLICATE'
#         ELSE 'UNIQUE'
#     END AS Duplicate_data
# FROM kmb_extraction.ocr
# LIMIT 500;
# """

query2 = """SELECT
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
"""
# SELECT
#     o.customer_name,
#     o.crn,
#     o.created_date,
#     CASE
#         WHEN COUNT(*) OVER (PARTITION BY o.customer_name, o.crn, DATE(o.created_date)) > 1
#         THEN 'DUPLICATE'
#         ELSE 'UNIQUE'
#     END AS duplicate_case
# FROM kmb_extraction.ocr o
# WHERE o.customer_name IS NOT NULL
#   AND o.crn IS NOT NULL;


# query2 = """
# SELECT
#     ocr.customer_name,
#     ocr.crn,
#     ocr.created_date
#     from kmb_extraction.ocr LIMIT 20;
# """


data = pd.read_sql(query2, connection)
print(data)