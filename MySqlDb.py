import mysql.connector

cnx = mysql.connector.connect(user='root', password='root@123',
                              host='localhost',
                              database='test_db')

cursor = cnx.cursor()
cursor.execute("drop table customers")
cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

print("Table created sucessfully!!")

cursor.execute('''insert into customers values("upendra","pune")''')
cnx.commit()
print("Record inserted!!")

cnx.close()
