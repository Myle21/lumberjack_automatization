import pyautogui
import time

while True:
    left = (900, 900)
    right = (1050, 900)
    im = pyautogui.screenshot()
    px_right_top = im.getpixel((1011, 634))
    px_left_top = im.getpixel((919, 634))
    if px_left_top != (211, 247, 255):
        pyautogui.click(right)
    else:
        if px_right_top != (211, 247, 255):
            pyautogui.click(left)