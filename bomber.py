import random

import pyautogui
import time


comments = ["Surprise MotherF*****", "Python Bot", "Hah hah hah"]

time.sleep(5)

while True:
    pyautogui.typewrite(comments[random.randrange(1, len(comments))])
    pyautogui.typewrite("\n")
    time.sleep(5)

