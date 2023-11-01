import PySimpleGUI as sg
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jayden00!",
    database="planeinfo"
)

cursor = mydb.cursor()

def main():
    layout = [
        [sg.Text('Add Flights')],
        [sg.Text('Origin:'), sg.InputText(key='-Origin-')],
        [sg.Text('Destination:'), sg.InputText(key='-Dest-')],
        [sg.Text('Date:'), sg.InputText(key='-Date-', readonly=True), sg.CalendarButton('Choose', target='-Date-', format='%d-%m-%Y')],
        [sg.Text('Number of Seats:'), sg.InputText(key='-NumSeats-')],
        [sg.Text('Price Economy:'), sg.InputText(key='-PriceEco-')],
        [sg.Text('Price First Class:'), sg.InputText(key='-PriceFClass-')],
        [sg.Button('Enter'), sg.Button('Exit')]
    ]

    # Create the window
    window = sg.Window('Plane Seat Booking System', layout)

    # Event loop
    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break

        elif event == 'Enter':
            query_insert = "INSERT INTO flightInfo (flightID, flightOrigin, flightDest, flightDate, numSeats, priceEco, priceFClass)  VALUES (%s, %s, %s, %s, %s, %s, %s)"

            origin = values['-Origin-']
            dest = values['-Dest-']
            date = values['-Date-']
            numSeats = values['-NumSeats-']
            priceEco = values['-PriceEco-']
            priceF = values['-PriceFClass-']

            # Convert date format from dd-mm-yyyy to yyyy-mm-dd
            date = '-'.join(date.split('-')[::-1])

            flightID = origin[0:3] + dest[0:3] + date[0:2] + date[3:5] + date[8:10]

            data = (flightID, origin, dest, date, numSeats, priceEco, priceF)
            cursor.execute(query_insert, data)

            mydb.commit()  # Commit the transaction to save changes to the database

            sg.popup('Added to Database')

    window.close()

if __name__ == '__main__':
    main()
