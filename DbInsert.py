import psycopg2

# Establishing the connection
conn = psycopg2.connect(database="postgres", user='postgres', password='root', host='127.0.0.1', port='5432')
# Setting auto commit false
conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# cursor.execute('''insert into vendors values(1,'upendra')''')

cursor.execute('''select * from vendors where vendor_id=1''')

result = cursor.fetchall()
print(result)

# Commit your changes in the database
conn.commit()
# print("Records inserted........")

# Closing the connection
conn.close()
