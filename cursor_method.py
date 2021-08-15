#python cursor_method.py

#import the library
import mysql.connector

# creating connection
conn = mysql.connector.connect(
  host="localhost",
  user="sammy",
  password="password",
  database ="dbTest"
)

# import the cursor from the connection (conn)
mycursor = conn.cursor()

mycursor.execute("SELECT * FROM MOVIE")

print(mycursor.fetchone())  # fetch the first row
print(mycursor.fetchmany(4))  # fetch the next 2 rows
print(mycursor.fetchall())  # fetch all the remaining rows
print(mycursor.fetchmany())  # the result set is now empty

# we close the cursor and conn both
mycursor.close()
conn.close()
