import pyautogui
import psutil
from time import sleep
import sys

if sys.argv[2] == 'essence':
    type = 'assets/essence.png'
elif sys.argv[2] == 'key':
    type = 'assets/key.png'

max_iter = int(sys.argv[1])

for i in range(max_iter):
    try:
        pyautogui.locateOnScreen('assets/shop.png', confidence=0.8)
    except:
        print("Shop not found, please open the token shop first")
        break

    flag = None
    for i in range(3):
        try:
            x, y = pyautogui.locateCenterOnScreen(type, confidence=0.8)
            pyautogui.click(x, y)
            flag = True
            break
        except:
            try:
                x, y = pyautogui.locateCenterOnScreen('assets/shop.png', confidence=0.8)
                pyautogui.click(x, y)
                pyautogui.moveTo(x, y + 100)
                pyautogui.scroll(-5000)
                flag = False
            except:
                flag = False
                break

    if flag:
        sleep(3)
    else:
        print("Something went wrong with finding the icon, terminating")
        break

    try:
        x, y = pyautogui.locateCenterOnScreen('assets/forge.png', confidence=0.8)
        pyautogui.click(x, y)
        sleep(3)
        x, y = pyautogui.locateCenterOnScreen('assets/add.png', confidence=0.8)
        pyautogui.click(x, y)
        sleep(3)
    except:
        print("Something went wrong with forging, terminating")
        break
