import random
import FreeSimpleGUI as sg

randomNumber = random.randint(1,100)
currentApples = 0 
appleGatherAmount = 50
upgradeAmount = 1
purchasedAuto = False
upgradeAutoAmount = 0
autoGatherAmount = 100
devMove = True

layout = [
    [sg.Text('Apple Game')],
    [sg.Button(f'Gather Apple ({upgradeAmount})', key='GatherApple')],
    [sg.Button(f'Upgrade Apple Gather Amount (Cost: {appleGatherAmount} apples)', key='upgradeButton')],
    [sg.Button(f'Buy Auto Apple Gatherer (Cost: {autoGatherAmount} apples)', key='buyAutoApple')],
    [sg.Text(size=(40,1), key='result')],
    [sg.Button('Ok', bind_return_key=True), sg.Button('Quit')]
        ]


if devMove == True:
    layout.append([sg.Button('Dev Move Apples (+1000)', key='devMoveApples')])
    layout.append([sg.Text('Developer Mode Enabled')])


# Create the window
window = sg.Window('Window Title', layout)



# Display and interact with the Window using an Event Loop
while True:
    #vars


    #/vars
    
    event, values = window.read(timeout=600)
    # Closes the window if the user clicks the X button or the Quit button
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == 'devMoveApples':
        currentApples += 1000
        window['result'].update(f'You have {currentApples} apples')
        window.refresh()

    if purchasedAuto == True:
        currentApples += upgradeAutoAmount
        window['result'].update(f'You have {currentApples} apples') 
        window.refresh()


    if event == 'GatherApple':
        currentApples += upgradeAmount
        window['result'].update(f'You have {currentApples} apples')
    
    # Upgrade button logic
    if event == 'upgradeButton':
        if currentApples < appleGatherAmount: # Not enough apples to upgrade
            window['result'].update(f'You need {appleGatherAmount} apples to upgrade')
            continue
        # Enough apples to upgrade
        currentApples -= appleGatherAmount
        appleGatherAmount += appleGatherAmount ** .5 # Increase cost for next upgrade
        appleGatherAmount = int(appleGatherAmount) # Make sure it's an integer
        upgradeAmount += 1 # Increase the gather amount

        window['upgradeButton'].update(f'Upgrade Apple Gather Amount (Cost: {appleGatherAmount} apples)')
        window['GatherApple'].update(f'Gather Apple ({upgradeAmount})')
        window['result'].update(f'You have {currentApples} apples')


    if event == 'buyAutoApple':
        if currentApples < autoGatherAmount:
            window['result'].update(f'You need {autoGatherAmount} apples to buy Auto Apple Gatherer')
            continue
        currentApples -= autoGatherAmount
        window['result'].update(f'You have {currentApples} apples')
        upgradeAutoAmount += 1
        autoGatherAmount += autoGatherAmount ** .5
        autoGatherAmount = int(autoGatherAmount)
        window['buyAutoApple'].update(f'Buy Auto Apple Gatherer (Cost: {autoGatherAmount} apples)')
        sg.popup_auto_close(f'You bought an Auto Apple Gatherer! It will gather {upgradeAutoAmount} apple every second.', auto_close_duration=3)
        purchasedAuto = True



        # while True:
        #     event, values = window.read(timeout=1000)  # Check for events every second
        #     if event == sg.WINDOW_CLOSED or event == 'Quit':
        #         break
        #     currentApples += 1
        #     window['result'].update(f'You have {currentApples} apples')
        # if event == sg.WINDOW_CLOSED or event == 'Quit':
        #     break
    

    

# Finish up by removing from the screen
window.close()