import mysql.connector

# Establish database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jayden00!",
    database="planeinfo"
)

def get_all_columns():
    """Retrieve all columns in all tables of the database"""
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")

    tables = [table[0] for table in mycursor.fetchall()]

    for table in tables:
        print(f"Table: {table}")
        mycursor.execute(f"SHOW COLUMNS FROM {table}")
        columns = [column[0] for column in mycursor.fetchall()]
        print("Columns: ", columns)
        print()

    mycursor.close()

# Call the function to retrieve and print all columns
get_all_columns()
