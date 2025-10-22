#! python3
import time
import pyautogui
from pynput import keyboard
from pynput.keyboard import Controller, Key


keyboard_controller = Controller()

def on_press(key):
    if key == Key.caps_lock:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['down']:
        pyautogui.moveTo(1500, 820, .3, pyautogui.easeInQuad)
        pyautogui.click()
        time.sleep(0.2)
        keyboard_controller.press(Key.space)
        keyboard_controller.release(Key.space)
    # After action_done is True, do nothing for any key except esc

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys

#1500 820