import PySimpleGUI as sg
import mysql.connector
import databaseOutputs as dbo

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jayden00!",
        database="planeinfo"
)

# get cursor object
cursor= db.cursor()


def main():
    layout = [
        [sg.Text('Databases')],
        [sg.Button('Flights'), sg.Button('Seats')]
    ]

    # Create the window
    window = sg.Window('Plane Seat Booking System', layout, size=(200,75), element_justification='c')

    # Event loop
    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break

        elif event == 'Flights':
            window.close()
            dbo.dbOutput("flightinfo")

        elif event == 'Seats':
            window.close()
            dbo.dbOutput("bookedseats")

    window.close()

if __name__ == '__main__':
    main()
