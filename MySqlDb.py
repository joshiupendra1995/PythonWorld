import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123456789",
    database="testdb"
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE devops (name VARCHAR(255), address VARCHAR(255))")
