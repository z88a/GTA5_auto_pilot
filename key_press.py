"""
Analog key input. 
"""
# %%
import win32con
import win32api
import time
key_map = {
    "0": 48, "1": 49, "2": 50, "3": 51, "4": 52, "5": 53, "6": 54, "7": 55, "8": 56, "9": 57,
    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
    "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90
}

def key_down(key):
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code,win32api.MapVirtualKey(vk_code,0),0,0)

def key_up(key):
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), win32con.KEYEVENTF_KEYUP, 0)
 
def key_press(key):
    key_down(key)
    time.sleep(0.02)
    key_up(key)
