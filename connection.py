import pymysql
import requests
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="neora770",
    db="sql_intro",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)
if connection.open:
    print("the connection is opened")