from fastapi import FastAPI
import pyodbc 
app = FastAPI()


cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=35.240.27.145;"
                      "Database=db_name;"
                      "Trusted_Connection=yes;")

#35.240.27.145
#goaplha
#imbEvent2019

cursor = cnxn.cursor()
print(cursor.execute('SELECT 1;'))

for row in cursor:
    print('row = %r' % (row,))

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
    