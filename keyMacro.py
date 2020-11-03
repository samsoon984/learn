import pyautogui as pg
from pynput.keyboard import Key, Listener
import time
import random 
import pygetwindow as gw
import win32gui




while True:
    _getWindow = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if _getWindow == "MapleStory":
        print(_getWindow)
        pg.press('c')
        time.sleep(1)
    else:
        print(_getWindow)
        time.sleep(1)

"""
def on_press(key):
    if key == Key.end:
        pyautogui.press("f")
        time.sleep(random.uniform(0, 1))
        pyautogui.press("4")
    

with Listener(on_press=on_press) as listener:
    listener.join()
"""