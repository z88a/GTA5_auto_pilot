from grabscreen import grab_screen
import cv2
import time

WINDOWS_SIZE = (0, 40, 800, 600)
last_time = time.time()
while True:
    screen0 = grab_screen(region=WINDOWS_SIZE)
    screen1 = cv2.cvtColor(screen0, cv2.COLOR_BGR2GRAY)
    screen2 = cv2.resize(screen1, (200, 125))

    cv2.imshow('window', screen1)
    cv2.waitKey(1)
    print('time:{}'.format(time.time() - last_time))
    last_time = time.time()
