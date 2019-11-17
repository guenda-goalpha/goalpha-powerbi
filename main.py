from fastapi import FastAPI
import pyodbc
import json
app = FastAPI()
import os
import psycopg2


@app.get("/api/{endpoint}")
def api(endpoint: str):
    try:
        items_as_dict={"Warning": "Access Denied! Check Endpoint"}
        conn = psycopg2.connect(host="35.240.25.3",database="goalpha", user="postgres", password="imbEvent2019")
        cursor1 = conn.cursor()
        cursor1.execute("SELECT * FROM goalpha.public.datas WHERE end_point = '"+endpoint+"'")
        query = cursor1.fetchall()
        for data in query:
            cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=35.240.27.145;DATABASE=goalpha;UID=goalpha;PWD=imbEvent2019')
            cursor = cnxn.cursor()
            query = cursor.execute(data[2])

            items_as_dict={}
            for datas in query:
                my_list = []
                for i in range(1,len(datas)):
                    my_list.append(datas[i])
                items_as_dict[str(datas[0])] = my_list
                my_list = []
                # items_as_dict[str(datas[0])] = datas[1]
    except Exception as e:
        items_as_dict = {"Warning": "Access Denied! Check Endpoint"}
    return items_as_dict
    
