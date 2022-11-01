import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time
from PIL import ImageGrab
from threading import Thread
from windowcapture import WindowCapture
from vision import Vision
from utils import *
from pages.sieges.sieges import Sieges
from time import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))
wincap = WindowCapture('BlueStacks App Player 1')

vision = Vision(Sieges.siege_tower_jpg)
# vision = Vision(Sieges.go_to_track)
loop_time = time()
home = True
sieges = False
boss_track = False

navigation_bot_running = False
siege_bot_is_running = False


def bot_ack(rectrangles):
    global home
    global sieges
    global boss_track
    if home & len(rectrangles) > 0:
        click_pos = rectrangles[0]
        click_pos = wincap.click_pos(click_pos)
        print(click_pos)
        click(click_pos)
        vision.change_needle(Sieges.go_to_track)
        sleep(2)
        home = False
        sieges = True
    elif sieges & len(rectrangles) > 0:
        click_pos = rectrangles[0]
        click_pos = wincap.click_pos(click_pos)
        print(click_pos)
        click(click_pos)
        vision.change_needle(Sieges.track_boss)
        sleep(2)
        sieges = False
        boss_track = True

    global navigation_bot_running
    navigation_bot_running = False

attack_boss = False
retry_boss = False
already_dead = False
back = False

def siege_bot(rectangles):
    global boss_track
    global attack_boss
    global retry_boss
    global back

    if boss_track & len(rectangles) > 0:
        click_pos = rectangles[0]
        click_pos = wincap.click_pos(click_pos)
        print(click_pos)
        click(click_pos)
        vision.change_needle(Sieges.go_to_track)
        sleep(2)
        boss_track = False
        attack_boss = True
    elif attack_boss

while True:

    screenshot = wincap.get_screenshot()
    # wincap.focus_window()
    # bbs = 'pages/home/icons/siege_tower_btn.png'
    rectangles = vision.find(screenshot, 0.8, 'points')

    cond = navigation_bot_running is False
    # print(cond)
    if cond:
        navigation_bot_running = True
        t = Thread(target=bot_ack, args=(rectangles,))
        t.start()

    if siege_bot_is_running is True and navigation_bot_running is False:
        siege_bot_is_running = True
        t = Thread(target=siege_bot, args=(rectangles,))
        t.start()


    # cv.imshow('Vision', screenshot)
    # print('FPS {}'.format(1 / (time() - loop_time)))
    # print('FPS {}'.format(ready))
    loop_time = time()
    if cv.waitKey(1) == ord('q'):
        break
    elif cv.waitKey(1) == ord('s'):
        ready = True

cv.destroyWindow()
print('done')
