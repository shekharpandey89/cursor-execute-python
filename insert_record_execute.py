#python insert_record_execute.py

#import the library
import mysql.connector

# creating connection to the database
conn = mysql.connector.connect(
  host="localhost",
  user="sammy",
  password="password",
  database="dbTest"
)

mycursor = conn.cursor()

# execute the query with their record value
query = 'INSERT INTO MOVIE (id, name, year) VALUES (%s, %s, %s)'
val = (7, "Merlin", 2001)


mycursor.execute(query,val)

# we commit(save) the records to the table
conn.commit()

print(mycursor.rowcount, "record(s) inserted.")
