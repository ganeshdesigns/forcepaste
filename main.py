import tkinter
import pyautogui
import time

time.sleep(5)
clipboard_content = tkinter.Tk().clipboard_get()
print( clipboard_content.split("\n"))

for i in clipboard_content.split("\n"):
    pyautogui.write(i, interval=0)
    pyautogui.press("return")