import time

import keyboard
import pyautogui
import cv2
import pyautogui
import win32api, win32con
import numpy as np
import random
import time

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def sleep(duration):
    time.sleep(duration)

while not keyboard.is_pressed('q'):
    print(f'Hi, {pyautogui.position()}')  # Press Ctrl+F8 to toggle the breakpoint.
    time.sleep(1)
