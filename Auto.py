import pyautogui
from PIL import Image

import os
import subprocess
 
id = "xxx xxx xxxx" # zoom id
psw = "enter password"


def initialize():
    subprocess.Popen("C:\\Users\Renz\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    while True:
        try:
            join_meeting_button = pyautogui.locateOnScreen("final2.png")
            if join_meeting_button != None:
                pyautogui.click(join_meeting_button)
                break
            else:
                print("Looking for 'Join Meeting' button...")
        except Exception as e: print(e)
    print("'Join Meeting' clicked!")


def input_id():
    while True:
        try:
            id_field = pyautogui.locateOnScreen("id_field.png")
            if id_field != None:
                pyautogui.typewrite(id)
                break
            else:
                print("Looking for id field...")
        except Exception as e: print(e)


def join1():
    while True:
        try:
            join_button = pyautogui.locateOnScreen('join.png')
            if join_button != None:
                pyautogui.click(join_button)
                break
            else:
                print("Looking for 'Join' button...")
        except Exception as e: print(e)
    print("'Join' clicked!")

def input_pw():
    while True:
        try:
            pw_field = pyautogui.locateOnScreen("meeting passcode.png")
            if pw_field != None:
                pyautogui.typewrite(psw)
                break
            else:
                print("Looking for input field...")
        except Exception as e: print(e)



def join2():
    while True:
        try:
            join2_button = pyautogui.locateOnScreen('join2.png')
            if join2_button != None:
                pyautogui.click(join2_button)
                break
            else:
                print("Looking for 'Join' button...")
        except Exception as e: print(e)


initialize()
input_id()
join1()
input_pw()
join2()
