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

def checkAndClick(positions):
    if len(positions) > 0:
        click_pos = positions[0]
        click_pos = wincap.click_pos(click_pos)
        click(click_pos)
        sleep(0.5)
        return True
    return False
while True:

    screenshot = wincap.get_screenshot()

    # can see siege button -> press it skip rest
    start = vision.find(screenshot, Sieges.start, 0.8)
    offline_msg = vision.find(screenshot, Sieges.offline_msg, 0.8)
    siege_tower_rec = vision.find(screenshot, Sieges.siege_tower_jpg, 0.8)
    sieges_rec = vision.find(screenshot, Sieges.go_to_track, 0.8)
    attack = vision.find(screenshot, Sieges.attack, 0.8)
    retry = vision.find(screenshot, Sieges.retry, 0.8)
    already_dead = vision.find(screenshot, Sieges.is_dead, 0.8)
    skip = vision.find(screenshot, Sieges.skip, 0.8)
    back = vision.find(screenshot, Sieges.back, 0.8)
    track_boss_rec = vision.find(screenshot, Sieges.track_boss, 0.8)
    failed = vision.find(screenshot, Sieges.failed, 0.8)

    print('=================================================')
    print(f'start {len(start) > 0}')
    print(f'offline_msg {len(offline_msg) > 0}')
    print(f'siege_tower_rec {len(siege_tower_rec) > 0}')
    print(f'sieges_rec {len(sieges_rec) > 0}')
    print(f'track_boss_rec {len(track_boss_rec) > 0}')
    print(f'attack {len(attack) > 0}')
    print(f'retry {len(retry) > 0}')
    print(f'already_dead {len(already_dead) > 0}')
    print(f'skip {len(skip) > 0}')
    print(f'back {len(back) > 0}')
    print(f'siege_failed {len(failed) > 0}')

    if len(start) > 0:
        checkAndClick(start)
    if checkAndClick(offline_msg):
        continue
    if checkAndClick(siege_tower_rec):
        continue
    if checkAndClick(failed):
        continue
    if len(already_dead) > 0 and len(back) > 0:
        checkAndClick(back)
        continue
    if checkAndClick(retry):
        continue
    if checkAndClick(attack):
        continue
    if checkAndClick(skip):
        continue
    if checkAndClick(track_boss_rec):
        continue
    if checkAndClick(sieges_rec):
        print('qq')
        continue

    ## best attack & back = back
    ## attack = attack



    # rectangles = vision.find(screenshot, Sieges.siege_tower_jpg, 0.8, 'rectangles')
    # rectangles = vision.find(screenshot, Sieges.siege_tower_jpg, 0.8, 'rectangles')


    # can see siege bosses -> press it skip rest
    # can see track bosses -> press it skip rest
    # exist boss -> go kill it
    # summon boss -> go kill it

    loop_time = time()
    if cv.waitKey(1) == ord('q'):
        break
    elif cv.waitKey(1) == ord('s'):
        ready = True
    sleep(2)
cv.destroyWindow()
print('done')
