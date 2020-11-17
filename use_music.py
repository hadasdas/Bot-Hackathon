
import pymysql
import requests
import random 
from connection import  connection
"""connection = pymysql.connect(
    host="localhost",
    user="root",
    password="neora770",
    db="sql_intro",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)
if connection.open:
    print("the connection is opened")"""

def get_url_music(num):
    #try:
        with connection.cursor () as cursor:
            query = f"SELECT url_music FROM music WHERE id={num}"
            cursor.execute (query)
            result = cursor.fetchall ()
            random_url_num=random.randint (0, 4)
            print(result[random_url_num]['url_music'])
    #except:
        #print ("Error")
get_url_music(0)