# This is a sample Python script
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# port cv2
import cv2
import pyautogui
import win32api, win32con
import numpy
import random
import time
import mss
import keyboard
from ScreenTarget import Target, Monitor

def grab_screen(monitor_number):
    sct = mss.mss()
    mon = sct.monitors[monitor_number]
    print(mon)
    monitor = {"top": mon["top"], "left": mon["left"], "width": 1920, "height": 1080, "mon": 2}
    return Monitor(mon["left"], mon["top"], 1920, 1080, numpy.asarray(sct.grab(monitor)))


def click(point):
    print(f'Click {point}')
    orig_pos = pyautogui.position()
    win32api.SetCursorPos((point[0], point[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(numpy.random.uniform(0.1, 0.5))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    win32api.SetCursorPos(orig_pos)

def sleep(duration):
    time.sleep(duration)

def find(key):
    monitor = grab_screen(2)
    needle = cv2.imread(key, cv2.IMREAD_UNCHANGED)
    result = cv2.matchTemplate(monitor.image, needle, cv2.TM_CCOEFF_NORMED)
    yloc, xloc = numpy.where(result >= .90)
    if len(yloc) > 0:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = needle.shape[1]
        h = needle.shape[0]
        return Target(True, (monitor.left + int(max_loc[0] + w / 2), int(max_loc[1] + h / 2)))
    else:
        return Target(False, (0, 0))


backpack = 'resources/icons/backpack.png'
siegeBtn = 'resources/icons/siege_tower_btn.png'
siegeLabel = 'resources/icons/siege_week_label.png'
goToTrackBosses = 'resources/icons/sieges_btn.png'

def lala2():
    needle = cv2.imread(siegeBtn, cv2.IMREAD_UNCHANGED)
    target = grab_screen(2)

    result = cv2.matchTemplate(target, needle, cv2.TM_CCOEFF_NORMED)
    print(result)
    yloc, xloc = numpy.where(result >= .80)
    if len(yloc) > 0:
        print(len(yloc))
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(max_loc)
        print(max_val)
        w = needle.shape[1]
        h = needle.shape[0]
        print(w)
        print(h)

        #print(target.shape)
        cv2.rectangle(target, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 255), 5)
        #cv2.rectangle(target, (100, 50), (125, 80), (0, 255, 255), -1)
        cv2.imwrite('new.png', target)
        cv2.imshow('343', cv2.imread('new.png', cv2.IMREAD_UNCHANGED))
        #target2 = cv2.imread('resources/qqq.png', cv2.IMREAD_UNCHANGED)
        #cv2.imshow('343', target2)
        cv2.waitKey()
        cv2.destroyAllWindows()
    else:
        print('nothing found')


def lala3():
    needle = cv2.imread(siegeBtn, cv2.IMREAD_UNCHANGED)
    target = grab_screen(2)
    ta = find(siegeBtn)

    print(ta.click_point)
    cv2.rectangle(target, ta.click_point, ta.click_point, (0, 255, 255), 5)
        #cv2.rectangle(target, (100, 50), (125, 80), (0, 255, 255), -1)
    cv2.imwrite('new.png', target)
    cv2.imshow('343', cv2.imread('new.png', cv2.IMREAD_UNCHANGED))
        #target2 = cv2.imread('resources/qqq.png', cv2.IMREAD_UNCHANGED)
        #cv2.imshow('343', target2)
    cv2.waitKey()
    cv2.destroyAllWindows()



def lala():
    while not keyboard.is_pressed('q'):
        home = find(siegeBtn)
        if home.found:
            print(f'Home {home}')
            print('I am on home screen, going to siege')
            click(home.click_point)
            sleep(1)
            sieges = find(goToTrackBosses)
            if sieges.found:
                print('Ready to siege')
                print(f'Home {sieges}')
                bosses = click(sieges.click_point)
                if sieges.found:
                    print('Ready to siege')
                    print(f'Home {sieges}')
                    click(sieges.click_point)
                else:
                    print('Cannot find sieges button')
            else:
                print('Cannot find sieges button')
        else:
            print('Cannot find siege button')

lala()