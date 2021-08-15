#python simple_execute_function.py

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

# iterate over result
for row in mycursor:
    print(row)

# we close the cursor and conn both
mycursor.close()
conn.close()


