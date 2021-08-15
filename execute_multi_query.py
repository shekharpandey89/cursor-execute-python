# python execute_multi.py

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

# query with format parameter style

query_1 = "select * from MOVIE"

query_2 = 'INSERT INTO MOVIE (id, name, year) VALUES (%s, %s, %s)'

queries = [query_1,query_2]

val = (8, "Series", 2001)

# returns an iterator
multiresults = mycursor.execute(";".join(queries), val, multi=True)

count = 1
for result in multiresults:

    # result is just like a cursor, so we can access all
    # attributes of the cursor
    print("query_{0} - {1} :".format(count, result.statement))
    if result.with_rows:
        for row in result:
            print(row)
        count = count + 1
    else:
        print("No result")

    print()

mycursor.close()
conn.close()