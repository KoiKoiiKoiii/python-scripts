import random
import FreeSimpleGUI as sg

moves = ['Rock', 'Paper', 'Scissors']
num1 = 0
num2 = 0

# Define the window's contents
layout = [
    [
        sg.Button('Rock'),
        sg.Button('Paper'),
        sg.Button('Scissors'),
        sg.Text(size=(10,1), key='aiWins'),
        sg.Text(size=(10,1), key='playerWins')
    ],
    
    [sg.Text(size=(40,1), key='yourMove')],
    [sg.Text(size=(40,1), key='result')],
    [sg.Text(size=(40,1), key='aiMove')],
    [sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    #vars

    aiMove = moves[random.randint(0,2)]

    #/vars

    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window. Use `event` because buttons return their key/label
    # as the event and not all buttons set an entry in `values` (which caused KeyError).

    window['yourMove'].update(f"You picked {event}!")
    window['result'].update(f"You tied!")
    window['aiMove'].update('The AI move was ' + aiMove)


    # Win conditions
    if event == 'Rock' and aiMove == 'Scissors':
        window['result'].update("You win! Rock crushes Scissors.")
        num2 += 1
    if event == 'Rock' and aiMove == 'Paper':
        window['result'].update("You lose! Paper covers Rock.")
        num1 += 1
    if event == 'Paper' and aiMove == 'Rock':
        window['result'].update("You win! Paper covers Rock.")
        num2 += 1
    if event == 'Paper' and aiMove == 'Scissors':
        window['result'].update("You lose! Scissors cut Paper.")
        num1 += 1
    if event == 'Scissors' and aiMove == 'Paper':
        window['result'].update("You win! Scissors cut Paper.")
        num2 += 1
    if event == 'Scissors' and aiMove == 'Rock':
        window['result'].update("You lose! Rock crushes Scissors.")
        num1 += 1
    # Update the win counts
    window['aiWins'].update(f"AI Wins: {num1}")
    window['playerWins'].update(f"Your Wins: {num2}")


# Finish up by removing from the screen
window.close()