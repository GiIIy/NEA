import PySimpleGUI as sg
import GrabFlightInfo

ORIGINS = GrabFlightInfo.grabOrigin()
DESTS = GrabFlightInfo.grabDest()
DATES = GrabFlightInfo.grabDates()

def main():
    layout = [
        [sg.Text('Search Flights')],
        [sg.Text('Origin:'), sg.OptionMenu(ORIGINS, key='-ORIGIN-')],
        [sg.Text('Destination:'), sg.OptionMenu(DESTS, key='-DEST-')],
        [sg.Text('Date'), sg.OptionMenu(values=["No Dates Found"],key='-DATES-')],
        [sg.Button('Search'), sg.Button('Exit')]
    ]

    # Create the window
    window = sg.Window('Plane Seat Booking System', layout)

    # Initialize selected destination
    selected_destination = None

    # Event loop
    while True:
        event, values = window.read(timeout=1000)
        orVal = values['-ORIGIN-']
        destVal = values['-DEST-']
        
        if orVal in ORIGINS and destVal in DESTS:
            updated_dates = [DATES[ORIGINS.index(orVal)]]

            if len(updated_dates) == 1:
                selected_dates = updated_dates[0]  # Store the selected date

            window['-DATES-'].update(values=updated_dates)

            if selected_dates is not None:
                window['-DATES-'].update(value=selected_dates)  # Set the selected date



        if orVal in ORIGINS:
            updated_dests = [DESTS[ORIGINS.index(orVal)]]

            if len(updated_dests) == 1:
                selected_destination = updated_dests[0]  # Store the selected destination

            window['-DEST-'].update(values=updated_dests)

            if selected_destination is not None:
                window['-DEST-'].update(value=selected_destination)  # Set the selected destination


        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break

        elif event == 'Search':
            sg.popup('Searching...')

    window.close()

if __name__ == '__main__':
    main()
