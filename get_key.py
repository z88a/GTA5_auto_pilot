import win32api as wapi
import time
import win32con

keyList = ["W", "A", "S", "D", win32con.VK_LEFT, win32con.VK_RIGHT, win32con.VK_UP, win32con.VK_DOWN1WASD, win32con.VK_ESCAPE]


def key_check():
    keys = []
    for key in keyList:
        if str(key).isdigit():
            if wapi.GetAsyncKeyState(key):
                keys.append(key)
        else:
            if wapi.GetAsyncKeyState(ord(key)):
                keys.append(key)
    return keys


if __name__ == "__main__":
    while True:
        keys = key_check()
        if len(keys) > 0:
            print(keys)
