import mysql.connector

def grabOrigin():
    # Establish database connection
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jayden00!",
        database="planeinfo"
    )

    cursor = mydb.cursor()

    # SQL command to select all information from the table
    table_name = "flightInfo"
    select_query = f"SELECT * FROM {table_name};"
    cursor.execute(select_query)
    result = cursor.fetchall()

    origins = []
    for row in result:
        origins.append(row[1])

    # Close the cursor and database connection
    cursor.close()
    mydb.close()

    return origins

def grabDest():
    # Establish database connection
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jayden00!",
        database="planeinfo"
    )

    cursor = mydb.cursor()

    # SQL command to select all information from the table
    table_name = "flightInfo"
    select_query = f"SELECT * FROM {table_name};"
    cursor.execute(select_query)
    result = cursor.fetchall()

    dests = []
    for row in result:
        dests.append(row[2])

    # Close the cursor and database connection
    cursor.close()
    mydb.close()

    return dests

def grabDates():
    # Establish database connection
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jayden00!",
        database="planeinfo"
    )

    cursor = mydb.cursor()

    # SQL command to select all information from the table
    table_name = "flightInfo"
    select_query = f"SELECT * FROM {table_name};"
    cursor.execute(select_query)
    result = cursor.fetchall()

    dates = []
    for row in result:
        dates.append(row[3].strftime('%d/%m/%Y'))

    # Close the cursor and database connection
    cursor.close()
    mydb.close()

    return dates
