import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nischay@123",
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE mydb")
print('ALL DONE');