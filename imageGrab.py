import time

import cv2
import mss
import numpy


def screen_record():
    try:
        from PIL import ImageGrab
    except ImportError:
        return 0

    # 800x600 windowed mode
    mon = (0, 40, 800, 640)

    title = "[PIL.ImageGrab] FPS benchmark"
    fps = 0
    last_time = time.time()

    while time.time() - last_time < 1:
        img = numpy.asarray(ImageGrab.grab(bbox=mon))
        fps += 1

        cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    return fps


def screen_record_efficient():
    # 800x600 windowed mode
    sct = mss.mss()

    monitor_number = 2
    mon = sct.monitors[monitor_number]
    print(mon)
    monitor = {"top": mon["top"], "left": mon["left"], "width": 1920, "height": 1080, "mon": 2}

    title = "[MSS] FPS benchmark"
    fps = 0
    last_time = time.time()

    while time.time() - last_time < 1:
        img = numpy.asarray(sct.grab(monitor))
        fps += 1

        cv2.imshow(title, img)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    return fps


print("PIL:", screen_record())
print("MSS:", screen_record_efficient())


def grabScreen(monitor_number):
    sct = mss.mss()
    mon = sct.monitors[monitor_number]
    print(mon)
    monitor = {"top": mon["top"], "left": mon["left"], "width": 1920, "height": 1080, "mon": 2}

    return numpy.asarray(sct.grab(monitor))


===============================
