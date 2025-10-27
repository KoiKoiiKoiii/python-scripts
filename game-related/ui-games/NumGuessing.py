import random
import FreeSimpleGUI as sg

randomNumber = random.randint(1,100)

layout = [
    [sg.Text('Guess a number between 1 and 100:')],
    [sg.Input(size=(40,1),key='guessedNumber', do_not_clear=False)],
    [sg.Text(size=(40,1), key='yourMove')],
    [sg.Text(size=(40,1), key='result')],
    [sg.Text(size=(40,1), key='aiMove')],
    [sg.Button('Ok', bind_return_key=True), sg.Button('Quit')]
        ]


# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    #vars


    #/vars

    event, values = window.read()
    # Closes the window if the user clicks the X button or the Quit button
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    
    try:
        guessedNumber = int(values['guessedNumber'])
    except ValueError:
        window['result'].update("Please enter a valid number!")
        continue
    window['yourMove'].update(f"You picked {values['guessedNumber']}!")

    if guessedNumber < 1 or guessedNumber > 100:
        window['result'].update("Number must be between 1 and 100!")
        continue
    if guessedNumber < randomNumber:
        window['result'].update("Too low! Try again.")
        continue
    if guessedNumber > randomNumber:
        window['result'].update("Too high! Try again.")
        continue
    if guessedNumber == randomNumber:
        window['result'].update("You guessed it! Congratulations!")
    

# Finish up by removing from the screen
window.close()