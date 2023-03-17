
import pyautogui
import time

try:
    f = open('./code.txt', 'r')
except FileNotFoundError:
    print("code.txt消すな!")

print("5秒後に開始")

time.sleep(5000)

pyautogui.write(f, 0.05)
