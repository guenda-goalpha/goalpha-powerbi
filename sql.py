import pyodbc 

cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=server_name;"
                        "Database=goaplha;"
                        "uid=goaplha;"
                        "pwd=imbEvent2019")

#35.240.27.145
#goaplha
#imbEvent2019

cursor = cnxn.cursor()
print(cursor.execute('SELECT * from T_KOKASHITJE;'))
