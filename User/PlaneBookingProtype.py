import PySimpleGUI as sg

def create_seat_layout(num_rows, num_cols):
    """Create the seat layout for the plane"""
    seats = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    return seats

def draw_seat_layout(window, seat_layout, start_row, num_rows):
    """Draw the seat layout on the GUI, starting from the specified row"""
    for row in range(start_row, start_row + num_rows):
        for col in range(len(seat_layout[row])):
            seat_text = seat_layout[row][col]
            button_key = f'-SEAT-{row}-{col}-'
            window[button_key].update(seat_text)
    window.refresh()

def update_seat_status(window, button_key):
    """Update the status of a seat on the GUI"""
    window[button_key].update(disabled=True, button_color=('white', 'red'))

def book_seat(window, seat_layout, row, col, start_row, num_rows):
    """Handle seat booking"""
    # Check if the seat is already booked
    if seat_layout[row][col] == 'X':
        sg.popup_error('This seat is already booked!')
    else:
        # Calculate the seat price
        seat_price = 100  # Example price for Now

        # Ask the user if they want to buy the ticket
        confirm_message = f"Seat Selected: Row {row+1}, Column {col+1}\nPrice: ${seat_price}"
        confirm_title = 'Confirm Seat Booking'
        confirm_popup = sg.popup_yes_no(confirm_message, title=confirm_title, button_color=('white', 'red'))

        if confirm_popup == 'Yes':
            # Update the seat status
            seat_layout[row][col] = 'X'
            button_key = f'-SEAT-{row}-{col}-'
            update_seat_status(window, button_key)
            draw_seat_layout(window, seat_layout, start_row, num_rows)  # Update the seat layout on the GUI

            # Update the balance
            current_balance = int(window['-BALANCE-'].Get()) if window['-BALANCE-'].Get() else 0
            new_balance = current_balance + seat_price
            window['-BALANCE-'].update(new_balance)

    window.refresh()  # Refresh the GUI to reflect the change
    window.bring_to_front()  # Bring the main window to front after closing the pop-up

def main():
    # Define the seat layout
    num_rows = 10  # Increase the number of rows
    num_cols = 6
    seat_layout = create_seat_layout(num_rows, num_cols)
    
    start_row = 0     # Starting row for scrolling
    
    # Create the GUI layout
    layout = [
        [sg.Text('Plane Seat Booking System')],
        [sg.Text('Select a seat to book')],
        [sg.Text('Balance:', size=(10, 1)), sg.Text('0', key='-BALANCE-')],
        [sg.Column(
            [[sg.Button('', key=f'-SEAT-{row}-{col}-', size=(4, 2)) for col in range(num_cols)] for row in range(num_rows)],
            scrollable=True, vertical_scroll_only=True, size=(400, 240),
            key='-SCROLLABLE-'
        )],
        [sg.Button('Go to Pay'), sg.Button('Exit')]
    ]

    # Create the window
    window = sg.Window('Plane Seat Booking System', layout)

    # Event loop
    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break

        if event.startswith('-SEAT-'):
            try:
                row, col = map(int, event.split('-')[2:4])
            except ValueError:
                continue

            book_seat(window, seat_layout, row, col, start_row, num_rows)  # Pass start_row

        elif event == 'Go to Pay':
            # Placeholder code, replace with your own logic
            sg.popup('Redirecting to payment page...')

        elif event.startswith('-SCROLLABLE-'):
            # Update the displayed seats based on the scroll position
            start_row = values['-SCROLLABLE-'][1]  # Get the top visible row
            draw_seat_layout(window, seat_layout, start_row, num_rows)

        draw_seat_layout(window, seat_layout, start_row, num_rows)

    window.close()

if __name__ == '__main__':
    main()
