"""
Capturing screen and keyboard event to each sample. 
"""
# %%
import cv2
from pynput import keyboard
from pynput.keyboard import Controller, Key, Listener
import time

from grabscreen import grab_screen
from key_press import *

WINDOWS_SIZE = (0, 40, 800, 600)
FIG_SIZE = (200, 125)

def press(key):
    if isinstance(key, keyboard.KeyCode):
        print(key.char)

        screen0 = grab_screen(region=WINDOWS_SIZE)

        grab_time = time.localtime(time.time())
        grab_time = time.strftime("%Y%m%d%H%M%S", grab_time)

        screen1 = cv2.cvtColor(screen0, cv2.COLOR_BGR2GRAY)
        screen2 = cv2.resize(screen1, FIG_SIZE)
        cv2.imshow('window', screen1)
        cv2.imwrite('E:/GAME/GTA5/data/' + grab_time + '_' + key.char + '.png', screen1)
    return False

def generate_sample():
    with Listener(on_press=press) as listener:
        listener.join()
    
# %%
# generate_sample()

# %%
