import os
import sys

import pyautogui

size = pyautogui.size()
center = (size[0]/2,size[1]/2)


pyautogui.moveTo(center)

n = 5

for i in range(n):
    center = list(center)
    center[0] += 100
    center = tuple(center)
    pyautogui.moveTo(center)
    print("oke")


while True:
    a = input()
    if a == "a":
        break