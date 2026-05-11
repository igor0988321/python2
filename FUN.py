import keyboard
import time
import pyautogui


time.sleep(5)

for i in range(50):
    # enter your word
    keyboard.write("")
    time.sleep(0.01)
    pyautogui.press("enter")