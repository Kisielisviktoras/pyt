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
    time.sleep(numpy.random.uniform(0.1, 0.5))
    # win32api.SetCursorPos(orig_pos)


def sleep(duration):
    time.sleep(duration)


def find(key, debug):
    monitor = grab_screen(2)
    needle = cv2.imread(key, cv2.IMREAD_UNCHANGED)
    result = cv2.matchTemplate(monitor.image, needle, cv2.TM_CCOEFF_NORMED)
    yloc, xloc = numpy.where(result >= .60)
    if len(yloc) > 0:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = needle.shape[1]
        h = needle.shape[0]

        target = Target(True, (monitor.left + int(max_loc[0] + w / 2), int(max_loc[1] + h / 2)))

        if debug:
            print(f'{key} found')
            # print((int(max_loc[0] + w / 2), int(max_loc[1] + h / 2)))
            res = cv2.rectangle(monitor.image, (int(max_loc[0] + w / 2), int(max_loc[1] + h / 2)),
                                (int(max_loc[0] + w / 2), int(max_loc[1] + h / 2)), (100, 255, 20), 20)
            res = cv2.rectangle(res, (int(max_loc[0] + 100), int(max_loc[1] + h / 2)),
                                (int(max_loc[0] + w / 2), int(max_loc[1] + h / 2)), (0, 0, 0), 10)
            cv2.imwrite(key + '_debug.png', res)

        return target
    else:
        if debug:
            print(f'CANNOT FIND {key}')
            cv2.imwrite('debug/screen_debug_screen.png', monitor.image)
            cv2.imwrite(key + '_debug.png', needle)
        return Target(False, (0, 0))


def wait_find(key, debug):
    count = 1
    max_retry = 5
    while count <= max_retry:
        res = find(key, debug)
        if res.found:
            return res
        else:
            print(f'Could not find {key}, retrying {count}/{max_retry}')
            sleep(0.5)
            count = count + 1

def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        print(hex(hwnd), win32gui.GetWindowText(hwnd))

#win32gui.EnumWindows(winEnumHandler, None)