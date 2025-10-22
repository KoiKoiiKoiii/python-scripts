import os
from tempfile import tempdir
import requests
import math
import random
import FreeSimpleGUI as sg
import tempfile
import requests
from PIL import Image

steamDevKey = '3009966D5F83B020E4E1949B13EEA5B3'
steamId = "76561198079996347"  # Replace with a valid Steam ID
temp_dir = tempfile.gettempdir()

layout = [
    [sg.Text('Steam Library Check')],
    [sg.Text(size=(60,1), key='output')],
    [sg.Image('', key='Image')],
    [sg.Text(size=(60,1), key='gameInfo')],
    [sg.Text(size=(60,1), key='gamePop')],
    [sg.Text(size=(60,1), key='playtime')],
    [sg.Text('Note: Ensure the Steam profile is public to retrieve game data.')],
    [sg.Text('SteamID:'), sg.Input(size=(40,1),key='steamId', do_not_clear=False, default_text=steamId)],
    [sg.Button('Check Library', bind_return_key=True), sg.Button('Quit')]
        ]
# Create the window
window = sg.Window('Steam Library Check', layout)

url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={steamDevKey}&steamid={steamId}&include_appinfo=true"
# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # Closes the window if the user clicks the X button or the Quit button
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'Check Library':
        window['output'].update("Checking library...")
        window.refresh()

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        window['output'].update(f"{data["response"]["game_count"]} total games.")
        window.refresh()

        randomGame = data["response"]["games"][math.floor(random.random() * data["response"]["game_count"])]
        gamePopurl = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1?appid={randomGame['appid']}"
        gamePopResponse = requests.get(gamePopurl)
        gamePopData = gamePopResponse.json()
        gamePop = gamePopData.get("response", {}).get("player_count", "N/A")
        


        window['gameInfo'].update("Grabbing a random game...")
        window.refresh()

        window['gameInfo'].update(f"Game Name: {randomGame['name']}")
        window['playtime'].update(f"Playtime: {randomGame['playtime_forever']} minutes")
        window['gamePop'].update(f"Current Players: {gamePop}")
        window.refresh()
        #(f"Random Game: {randomGame['name']}")
        #print(f"App ID: {randomGame['appid']}")
        #print(f"Playtime: {randomGame['playtime_forever']} minutes")
        #print(f"Current Players: {gamePop}")


        #if "games" in data["response"]:
            #for game in data["response"]["games"]:
                #gamePopurl = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1?appid={game['appid']}"
                #gamePopResponse = requests.get(gamePopurl)
                #gamePopData = gamePopResponse.json()
                #gamePop = gamePopData.get("response", {}).get("player_count", "N/A")


                #print(f"Game Name: {game['name']}, App ID: {game['appid']}, Playtime: {game['playtime_forever']} minutes. Current Players: {gamePop}")

        #else:
            #print("No games found or profile is private.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}") 



