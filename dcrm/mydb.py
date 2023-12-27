import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "richa",
)

#prepare cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE crmdata")

print("all done!")