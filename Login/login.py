import PySimpleGUI as sg


def main():
    layout = [
        [sg.Text('Add Flights')],
        [sg.Text('Username:'), sg.InputText()],
        [sg.Text('Password:'), sg.InputText('', password_char='*')],
        [sg.Button('Register'), sg.Button('Login'), sg.Button('Exit')]
    ]

    # Create the window
    window = sg.Window('Plane Seat Booking System', layout)

    # Event loop
    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break

        if event in ('Login'):
            print(values)

        if event in ('Register'):
            if len(values[1]) < 8:
                sg.popup('Password must be at least 8 characters')
            else:
                sg.popup('Registered')
        







    window.close()

if __name__ == '__main__':
    main()
