import mysql.connector
import PySimpleGUI as sg

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jayden00!",
    database="planeinfo"
)

# get cursor object
cursor = db.cursor()

def dbOutput(table_name):
    # execute your query
    cursor.execute(f"SELECT * FROM {table_name}")    
    # fetch column names from cursor description
    column_names = [desc[0] for desc in cursor.description]

        # fetch all the matching rows 
    result = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()

    headings = column_names
    data = result

    layout = [[sg.Table(data, headings=headings, justification='left', key='-TABLE-')],]
    window = sg.Window("Title", layout, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        print(event, values)

    window.close()