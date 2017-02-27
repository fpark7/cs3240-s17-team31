# Felix Park
# fjp7mb

import psycopg2
import csv

def analyzeData(db_name):
    PG_USER = "postgres"
    PG_USER_PASS = "qwerty"
    PG_DATABASE = db_name
    PG_HOST_INFO = " host=/tmp/"  # use "" for OS X or Windows

    # Connect to an existing database
    conn = psycopg2.connect("dbname=" + PG_DATABASE + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)
    print("** Connected to database.")
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM test;")

    # print("** Output from SQL SELECT: ", cur.fetchone())
    rows = cur.fetchall()
    for a in rows:
        print(a)

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()
    print("** Closed connection and database.  Bye!.")