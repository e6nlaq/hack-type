
import pyautogui
import time

try:
    f = open('./code.txt', 'r')
except FileNotFoundError:
    print("code.txt消すな!")

print("5秒後に開始")
data = f.read()

time.sleep(5)

pyautogui.write(data, 0.01)
