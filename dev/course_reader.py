# Felix Park
# fjp7mb

import psycopg2
import csv

def load_course_database( db_name, csv_filename):
    PG_USER = "postgres"
    PG_USER_PASS = "qwerty"
    PG_DATABASE = db_name
    PG_HOST_INFO = " host=/tmp/"  # use "" for OS X or Windows

    # Connect to an existing database
    conn = psycopg2.connect("dbname=" + PG_DATABASE + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)
    print("** Connected to database.")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # deptID courseNum semester meetingType seatsTaken seatsOffered instructor
    # Execute a command: this creates a new table, but first removes it if it's there already
    cur.execute("DROP TABLE IF EXISTS test;")
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, deptID varchar, courseNum integer, semester integer, meetingType varchar, seatsTaken integer, seatsOffered integer, instructor varchar);")
    print("** Created table.")

    with open(csv_filename, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Pass data to fill a query placeholders and let Psycopg perform
            # the correct conversion (no more SQL injections!)
            cur.execute("INSERT INTO test (deptID, courseNum, semester, meetingType, seatsTaken, seatsOffered, instructor) VALUES (%s, %s, %s, %s, %s, %s, %s)", tuple(row))
        print("** Exectuted SQL INSERT into database.")
    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM test;")

    #print("** Output from SQL SELECT: ", cur.fetchone())
    rows = cur.fetchall()
    for a in rows:
        print(a)

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()
    print("** Closed connection and database.  Bye!.")

if __name__ == "__main__":
    load_course_database("course1", "seas-courses-5years.csv")