# %%
from grabscreen import grab_screen
from get_key import key_check
import cv2
import time
import win32con

WINDOWS_SIZE = (0, 40, 800, 600)
FIG_SIZE = (200, 150)

PAUSE = False
last_time = time.time()
time.sleep(20)
while True:
    if PAUSE:
        break
    screen0 = grab_screen(region=WINDOWS_SIZE)
    screen1 = cv2.cvtColor(screen0, cv2.COLOR_BGR2GRAY)
    screen2 = cv2.resize(screen1, FIG_SIZE)
    grab_time = time.time()
    # grab_time1 = time.strftime("%Y%m%d%H%M%S", grab_time)
    keys = key_check()
    str_keys =''
    for item in keys :
        str_keys = str_keys + str(item)
    cv2.imshow('window', screen1)
    cv2.waitKey(1)
    cv2.imwrite('E:/GAME/GTA5/data/' + str(grab_time) + '_' + str_keys + '.png', screen2)
    print(str_keys)
    print('time:{}'.format(time.time() - last_time))
    last_time = time.time()
    if win32con.VK_ESCAPE in keys:
        PAUSE = True

# %%
