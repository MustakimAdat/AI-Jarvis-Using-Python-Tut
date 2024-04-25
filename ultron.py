from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Started The Jarvis : Wait For Few Seconds More")
from Main import MainTaskExecution
import wikipedia
import datetime
import webbrowser
import os
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests
import psutil
from time import sleep
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
# from notifypy import Notify
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web

hour = int(datetime.datetime.now().hour)

def MainExecution():
    Speak("Hello Sir")

    if hour>=0 and hour<12:
        Speak("Good Morning!")

    elif hour>=12 and hour<18:
        Speak("Good Afternoon!")

    else:
        Speak("Good Evening!")

    Speak("I'm Jarvis, I'm Ready To Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        if "jarvis" in Data.lower(): # check if "jarvis" is in the user's input
            ValueReturn = MainTaskExecution(Data)
            if ValueReturn==True:
                pass

            elif len(Data)<3:
                pass

            elif "whatsapp message" in Data:
                pass

            elif "turn on the tv" in Data:# Specific COmmand
                Speak("Ok..Turning On The Android TV")

            elif "set alarm" in Data:
                from Features_def import Alarm
                Alarm(Data)

# chrome auto starts

            elif "new tab" in Data:
                Speak("Ok..Opening New Tab")
                press_and_release('ctrl + t')

            elif "close tab" in Data:
                Speak("Ok..Closing Tab")
                press_and_release('ctrl + w')

            elif "new window in browser" in Data:
                Speak("Ok..Opening New Window")
                press_and_release('ctrl + n')

            elif "history in webbrowser" in Data:
                Speak("Ok..Opening History")
                press_and_release('ctrl + h')

            elif "download in browser" in Data:
                Speak("Ok.. Opening Downloads")
                press_and_release('ctrl + j')

            elif "bookmark" in Data:
                Speak("Ok..Bookmarking The Website")
                press_and_release('ctrl + d')
                press('enter')

            elif "incognito" in Data:
                Speak("Ok..Opening Incognito Mode")
                press_and_release('Ctrl + Shift + n')

            elif "switch tab" in Data:
                Speak("Ok..Switching Tabs")
                tab = Data.replace("switch tab ", "")
                Tab = tab.replace("to","")      
                num = Tab
                bb = f'ctrl + {num}'
                press_and_release(bb)

# chrome auto ends


# Youtube Auto starts

            elif "pause" in Data:
                Speak("Ok..Pausing")
                press('space bar')

            elif "resume" in Data:
                Speak("Ok..Resuming")
                press('space bar')

            elif "full screen" in Data:
                Speak("Ok..Full Screen")
                press('f')

            elif "film screen" in Data:
                Speak("Ok..Film Screen")
                press('t')

            elif "skip" in Data:
                Speak("Ok..Skipping")
                press('l')

            elif "back" in Data:
                Speak("Ok..Back")
                press('j')

            elif "increase speed" in Data:
                Speak("Ok..Increasing Speed")
                press_and_release('SHIFT + .')

            elif "decrease speed" in Data:
                Speak("Ok..Decreasing Speed")
                press_and_release('SHIFT + ,')

            elif "search in youtube" in Data:
                click(x=667, y=146)
                Speak("What To Search Sir ?")
                search = MicExecution()
                write(search)
                sleep(0.8)
                press('enter')

            elif "my channel" in Data:
                Speak("Ok..Opening Your Channel")
                web.open("https://www.youtube.com/channel/UCyFtY8oOXEY4Y0bN1QYNpug")

            elif "next video" in Data:
                Speak("Ok..Next")
                press_and_release('SHIFT + n')

            elif "download" in Data:
                from Features_def import DownloadYouTube
                DownloadYouTube()

# Youtube Auto Stops
        
            elif "temperature" in Data:
                from Features_def import Temp
                Temp(Data)


            elif "speed test" in Data:
                from Features_def import SpeedTest
                SpeedTest()

            elif "call" in Data:
                from Automations import WhatsappCall
                name = Data.replace("call ","")
                name = name.replace("jarvis ","")
                Name = str(name)
                WhatsappCall(Name)

            elif "show chat" in Data:
                Speak("With Whom ?")
                name = MicExecution()
                from Automations import WhatsappChat
                WhatsappChat(name)

            elif 'my location' in Data:
                from Features_def import My_Location
                My_Location()

            elif 'where is' in Data:
                from Automations import GoogleMaps
                Place = Data.replace("where is ","")
                Place = Place.replace("jarvis" , "")
                GoogleMaps(Place)

            elif 'online' in Data:
                from Automations import OnlinClass
                Speak("Tell Me The Name Of The Class .")
                Class = MicExecution()
                OnlinClass(Class)

            elif 'make a note' in Data:
                from Automations import Notepad
                Notepad()

            elif 'time table' in Data:
                from Automations import TimeTable
                TimeTable()

            elif 'corona cases' in Data:
                from Features_def import CoronaVirus
                Speak("Which Country's Information ?")
                cccc = MicExecution()
                CoronaVirus(cccc)

            elif 'How much is the charging' in Data or 'how much is the charging' in Data:
                battery = psutil.sensors_battery()
                print(f"Battery charge: {battery.percent}%")
                Speak("Battery charge: {battery.percent}%".format(battery=battery))

            elif 'Change window' in Data or 'change window' in Data:
                Speak("Ok..Changing The Tab")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                sleep(1)
                pyautogui.keyUp("alt")

            elif 'windows' in Data:
                Speak("Ok..Opening Windows")
                press('windows')

            elif 'search on windows' in Data:
                press_and_release('windows + s')

            elif 'home screen' in Data:
                Speak("Ok..Redirecting You To Home Screen")
                press_and_release('windows + m')

            elif "Hey Jarvis" in Data:
                ("Yes Sir! What can i do for you")

            elif 'youtube' in Data:
                Speak("what you will like to watch ?")
                qrry = MicExecution().lower()
                kit.playonyt(f"{qrry}")

            elif 'search on youtube' in Data:
                Data = Data.replace("search on youtube", "")
                webbrowser.open(f"www.youtube.com/results?search_query={Data}")

            elif 'close chrome' in Data:
                os.system("taskkill /f /im chrome.exe")
                Speak("Chrome has been closed")

            elif 'close youtube' in Data:
                os.system("taskkill /f /im msedge.exe")

            elif 'the time' in Data or 'what time is it' in Data:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                Speak(f"Sir, the time is {strTime}")

            elif 'the date' in Data or 'what date is today' in Data:
                strDate = datetime.datetime.now().strftime("%d %B %Y")
                Speak(f"Sir, today's date is {strDate}")

            elif 'the day' in Data or 'What day is it today' in Data:
                today = datetime.datetime.now().strftime("%A")
                Speak(f"Sir, today is {today}")
            
            elif "close command prompt" in Data:
                os.system("taskkill /f /im cmd.exe")

            elif "shut down the system" in Data:
                os.system("shutdown /s /t 5")

            elif "restart the system" in Data:
                os.system("shutdown /r /t 5")

            elif "Lock the system" in Data:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif 'google god mode' in Data:
                Speak("what should I search ?")
                qry = MicExecution().lower()
                webbrowser.open(f"{qry}")

            elif "take screenshot" in Data:
                Speak('tell me a name for the file')
                name = MicExecution().lower()
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                Speak("screenshot saved")

            elif "volume up" in Data:
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")

            elif "volume down" in Data:
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")

            elif "mute" in Data:
                pyautogui.press("volumemute")

            elif "scroll down" in Data:
                pyautogui.scroll(1000)

            elif 'type' in Data: #10
                Data = Data.replace("type", "")
                pyautogui.write(f"{Data}")

            elif 'close window' in Data:
                pyautogui.hotkey('ctrl', 'shift', 'w')

            elif 'good bye jarvis' in Data:
                Speak("Ok Sir, Bye")
                break

            else:                    
                Reply = ReplyBrain(Data)
                Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
    else:
        pass

ClapDetect()
