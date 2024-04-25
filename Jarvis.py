from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Started The Jarvis : Wait For Few Seconds More")
from Main import MainTaskExecution
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
from playsound import playsound
playsound("C:\\Users\\HP\\Desktop\\JARVIS-ChatGPT-main (Github)\\Assistant\\sounds\\data_writing.mp3")

hour = int(datetime.datetime.now().hour)

def MainExecution():
    pyautogui.press('esc')
    time.sleep(1)
    Speak("Verification successful")
    time.sleep(1)

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

        if "jarvis" in Data.lower() or "javed" in Data.lower() or "jarves" in Data.lower() or "religious" in Data.lower() or "Jarvis" in Data.lower() or "jar" in Data.lower(): # check if "jarvis" is in the user's input
            ValueReturn = MainTaskExecution(Data)
            if ValueReturn==True:
                pass

            elif len(Data)<3:
                pass

            elif "turn on the tv" in Data:# Specific COmmand
                Speak("Ok..Turning On The Android TV")

            elif "alarm" in Data: # new functionality for setting an alarm
                   Speak("Ok..Setting The Alarm")
                   from Features_def import set_alarm
                   set_alarm()

            elif "i am getting bored" in Data or "I'm getting board" in Data or "I'm Getting Board" in Data:
                from Automations import entertainment
                entertainment()

            if "jarvis" in Data.lower() or "javed" in Data.lower() or "jarves" in Data.lower() or "religious" in Data.lower() or "Jarvis" in Data.lower() or "jar" in Data.lower():
                playsound("C:\\Users\\HP\\Desktop\\JARVIS-ChatGPT-main (Github)\\Assistant\\sounds\\system_online_bleep.mp3")
                        
# chrome auto starts

            elif "new" in Data.lower() and "tab" in Data.lower():
                Speak("Ok..Opening New Tab")
                press_and_release('ctrl + t')

            elif "close" in Data.lower() and "tab" in Data.lower():
                Speak("Ok..Closing Tab")
                press_and_release('ctrl + w')

            elif "new" in Data.lower() and "window" in Data.lower() and ("webbrowser" in Data.lower() or "browser" in Data.lower()):
                Speak("Ok..Opening New Window")
                press_and_release('ctrl + n')

            elif "history" in Data.lower() and ("webbrowser" in Data.lower() or "browser" in Data.lower()):
                Speak("Ok..Opening History")
                press_and_release('ctrl + h')

            elif "download" in Data.lower() and ("webbrowser" in Data.lower() or "browser" in Data.lower()):
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

            elif "search in youtube" in Data or "search on youtube" in Data:
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

# Auomations starts

            if "video call" in Data:
                from Automations import WhatsappVideoCall
                name = Data.replace("video call ","")
                name = name.replace("jarvis ","")
                Name = str(name)
                WhatsappVideoCall(Name)

            elif "call" in Data:
                from Automations import WhatsappCall
                name = Data.replace("call ","")
                name = name.replace("jarvis ","")
                Name = str(name)
                WhatsappCall(Name)

            elif 'whatsapp message' in Data:
                name = Data.replace("whatsapp message","")
                name = name.replace("send ","")
                name = name.replace("to ","")
                name = name.replace("jarvis ","")
                name = name.replace("messages ","")
                Name = str(name)
                Speak(f"Whats The Message For {Name}")
                MSG = MicExecution()
                from Automations import WhatsappMsg
                WhatsappMsg(Name,MSG)

            elif "show chat" in Data:
                Speak("With Whom ?")
                name = MicExecution()
                from Automations import WhatsappChat
                WhatsappChat(name)

            elif "my location" in Data.lower():
                from Features_def import My_Location
                My_Location()

            elif 'where is' in Data:
                from Automations import GoogleMaps
                Place = Data.replace("where is ","")
                Place = Place.replace("jarvis" , "")
                GoogleMaps(Place)

            elif 'online class' in Data:
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

            elif "send email" in Data.lower():
                from Automations import send_email
                send_email()

# Auomations stops

            elif 'corona cases' in Data:
                from Features_def import CoronaVirus
                Speak("Which Country's Information ?")
                cccc = MicExecution()
                CoronaVirus(cccc)

            elif 'how much is the charging' in Data or 'how much charging is left' in Data or 'what is the percentage of charging left in my laptop' in Data:
                battery = psutil.sensors_battery()
                print(f"Your laptop is on: {battery.percent}%")
                Speak("Your laptop is on: {battery.percent}%".format(battery=battery))

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

            elif "Jarvis" in Data or "jarvis" in Data or "javed" in Data or "jarves" in Data or "religious" in Data or "Jarvis" in Data or "jar" in Data:
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

            elif 'the time' in Data or 'what time is it' in Data or 'what date is it today' in Data:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                Speak(f"Sir, the time is {strTime}")

            elif 'the date' in Data or 'what date is today' in Data or 'what is the date today' in Data:
                strDate = datetime.datetime.now().strftime("%d %B %Y")
                Speak(f"Sir, today's date is {strDate}")

            elif 'the day' in Data or 'what day is it today' in Data or 'what is the day today' in Data:
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

            elif "volume up" in Data or "increase the volume" in Data:
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

            elif "volume down" in Data or "decrease the volume" in Data:
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

            elif 'close the window' in Data:
                pyautogui.hotkey('ctrl', 'shift', 'w')

            elif 'good bye jarvis' in Data or 'goodbye jarvis' in Data or 'good bye jarvis' in Data:
                Speak("Ok Sir, Bye")
                playsound("C:\\Users\\HP\\Desktop\\JARVIS-ChatGPT-main (Github)\\Assistant\\sounds\\sleep.mp3")
                break

            else:

                from DataBase.ChatBot.ChatBot import ChatterBot

                reply = ChatterBot(Data)

                Speak(reply)

#################################################################################################################

if __name__ == "__main__":

    playsound("C:\\Users\\HP\\Desktop\\JARVIS-ChatGPT-main (Github)\\Assistant\\sounds\\wake.mp3")
    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read('C:\\Users\\HP\\Desktop\\AI Jarvis Using Python Tut\\Face-Recognition-main\\trainer\\trainer.yml')   #load trained model
    cascadePath = "C:\\Users\\HP\\Desktop\\AI Jarvis Using Python Tut\\Face-Recognition-main\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


    id = 2 #number of persons you want to Recognize


    names = ['','zeno']  #names, leave first empty bcz counter starts from 0


    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight

# Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

# flag = True

    while True:

        ret, img =cam.read() #read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
            )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

        # Check if accuracy is less them 100 ==> "0" is perfect match 
            if (accuracy < 100):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                MainExecution()

            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                Speak("Verification Failed")
        
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

# Do a bit of cleanup
    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()

# face lock