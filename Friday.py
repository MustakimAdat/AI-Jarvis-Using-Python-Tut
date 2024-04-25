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
import psutil #pip install psutil
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
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from mainGUI.form import Ui_mainGUIfile
import sys
playsound("C:\\Users\\HP\\Desktop\\JARVIS-ChatGPT-main (Github)\\Assistant\\sounds\\data_writing.mp3")

hour = int(datetime.datetime.now().hour)

class MainThread(QThread):

    def __init__(self): 
        super(MainThread,self).__init__()

    def run(self):
        self.MainExecution()

    def MainExecution(self):
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

            self.Data = self.MicExecution()
            self.Data = str(self.Data).replace(".","")

            if "jarvis" in self.Data.lower() or "javed" in self.Data.lower() or "jarves" in self.Data.lower() or "religious" in self.Data.lower() or "Jarvis" in self.Data.lower() or "jar" in self.Data.lower(): # check if "jarvis" is in the user's input
                ValueReturn = MainTaskExecution(self.Data)
                if ValueReturn==True:
                    pass

                elif len(self.Data)<3:
                    pass

                elif "turn on the tv" in self.Data:# Specific COmmand
                    Speak("Ok..Turning On The Android TV")

                elif "alarm" in self.Data: # new functionality for setting an alarm
                    Speak("Ok..Setting The Alarm")
                    from Features_def import set_alarm
                    set_alarm()

                elif "i am getting bored" in self.Data or "I'm getting board" in self.Data or "I'm Getting Board" in self.Data:
                    from Automations import entertainment
                    entertainment()

                # if "jarvis" in self.Data.lower() or "javed" in self.Data.lower() or "jarves" in self.Data.lower() or "religious" in self.Data.lower() or "Jarvis" in self.Data.lower() or "jar" in self.Data.lower():
                #     playsound("C:\\Users\\HP\\Desktop\\JARVIS-ChatGPT-main (Github)\\Assistant\\sounds\\system_online_bleep.mp3")
                            
    # chrome auto starts

                elif "new" in self.Data.lower() and "tab" in self.Data.lower():
                    Speak("Ok..Opening New Tab")
                    press_and_release('ctrl + t')

                elif "close" in self.Data.lower() and "tab" in self.Data.lower():
                    Speak("Ok..Closing Tab")
                    press_and_release('ctrl + w')

                elif "new" in self.Data.lower() and "window" in self.Data.lower() and ("webbrowser" in self.Data.lower() or "browser" in self.Data.lower()):
                    Speak("Ok..Opening New Window")
                    press_and_release('ctrl + n')

                elif "history" in self.Data.lower() and ("webbrowser" in self.Data.lower() or "browser" in self.Data.lower()):
                    Speak("Ok..Opening History")
                    press_and_release('ctrl + h')

                elif "download" in self.Data.lower() and ("webbrowser" in self.Data.lower() or "browser" in self.Data.lower()):
                    Speak("Ok.. Opening Downloads")
                    press_and_release('ctrl + j')

                elif "bookmark" in self.Data:
                    Speak("Ok..Bookmarking The Website")
                    press_and_release('ctrl + d')
                    press('enter')

                elif "incognito" in self.Data:
                    Speak("Ok..Opening Incognito Mode")
                    press_and_release('Ctrl + Shift + n')

                elif "switch tab" in self.Data:
                    Speak("Ok..Switching Tabs")
                    tab = self.Data.replace("switch tab ", "")
                    Tab = tab.replace("to","")      
                    num = Tab
                    bb = f'ctrl + {num}'
                    press_and_release(bb)

    # chrome auto ends


    # Youtube Auto starts

                elif "pause" in self.Data:
                    Speak("Ok..Pausing")
                    press('space bar')

                elif "resume" in self.Data:
                    Speak("Ok..Resuming")
                    press('space bar')

                elif "full screen" in self.Data:
                    Speak("Ok..Full Screen")
                    press('f')

                elif "film screen" in self.Data:
                    Speak("Ok..Film Screen")
                    press('t')

                elif "skip" in self.Data:
                    Speak("Ok..Skipping")
                    press('l')

                elif "back" in self.Data:
                    Speak("Ok..Back")
                    press('j')

                elif "increase speed" in self.Data:
                    Speak("Ok..Increasing Speed")
                    press_and_release('SHIFT + .')

                elif "decrease speed" in self.Data:
                    Speak("Ok..Decreasing Speed")
                    press_and_release('SHIFT + ,')

                elif "search in youtube" in self.Data or "search on youtube" in self.Data:
                    click(x=667, y=146)
                    Speak("What To Search Sir ?")
                    search = MicExecution()
                    write(search)
                    sleep(0.8)
                    press('enter')

                elif "my channel" in self.Data:
                    Speak("Ok..Opening Your Channel")
                    web.open("https://www.youtube.com/channel/UCyFtY8oOXEY4Y0bN1QYNpug")

                elif "next video" in self.Data:
                    Speak("Ok..Next")
                    press_and_release('SHIFT + n')

                elif "download" in self.Data:
                    from Features_def import DownloadYouTube
                    DownloadYouTube()

    # Youtube Auto Stops
            
                elif "temperature" in self.Data:
                    from Features_def import Temp
                    Temp(self.Data)

                elif "speed test" in self.Data:
                    from Features_def import SpeedTest
                    SpeedTest()

    # Auomations starts

                if "video call" in self.Data:
                    from Automations import WhatsappVideoCall
                    name = self.Data.replace("video call ","")
                    name = name.replace("jarvis ","")
                    Name = str(name)
                    WhatsappVideoCall(Name)

                elif "call" in self.Data:
                    from Automations import WhatsappCall
                    name = self.Data.replace("call ","")
                    name = name.replace("jarvis ","")
                    Name = str(name)
                    WhatsappCall(Name)

                elif 'whatsapp message' in self.Data:
                    name = self.Data.replace("whatsapp message","")
                    name = name.replace("send ","")
                    name = name.replace("to ","")
                    name = name.replace("jarvis ","")
                    name = name.replace("messages ","")
                    Name = str(name)
                    Speak(f"Whats The Message For {Name}")
                    MSG = MicExecution()
                    from Automations import WhatsappMsg
                    WhatsappMsg(Name,MSG)

                elif "show chat" in self.Data:
                    Speak("With Whom ?")
                    name = MicExecution()
                    from Automations import WhatsappChat
                    WhatsappChat(name)

                elif "my location" in self.Data.lower():
                    from Features_def import My_Location
                    My_Location()

                elif 'where is' in self.Data:
                    from Automations import GoogleMaps
                    Place = self.Data.replace("where is ","")
                    Place = Place.replace("jarvis" , "")
                    GoogleMaps(Place)

                elif 'online class' in self.Data:
                    from Automations import OnlinClass
                    Speak("Tell Me The Name Of The Class .")
                    Class = MicExecution()
                    OnlinClass(Class)

                elif 'make a note' in self.Data:
                    from Automations import Notepad
                    Notepad()

                elif 'time table' in self.Data:
                    from Automations import TimeTable
                    TimeTable()

                elif "send email" in self.Data.lower():
                    from Automations import send_email
                    send_email()

    # Auomations stops

                elif 'corona cases' in self.Data:
                    from Features_def import CoronaVirus
                    Speak("Which Country's Information ?")
                    cccc = MicExecution()
                    CoronaVirus(cccc)

                elif 'how much is the charging' in self.Data or 'how much charging is left' in self.Data or 'what is the percentage of charging left in my laptop' in self.Data:
                    battery = psutil.sensors_battery()
                    print(f"Your laptop is on: {battery.percent}%")
                    Speak("Your laptop is on: {battery.percent}%".format(battery=battery))

                elif 'Change window' in self.Data or 'change window' in self.Data:
                    Speak("Ok..Changing The Tab")
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    sleep(1)
                    pyautogui.keyUp("alt")

                elif 'windows' in self.Data:
                    Speak("Ok..Opening Windows")
                    press('windows')

                elif 'search on windows' in self.Data:
                    press_and_release('windows + s')

                elif 'home screen' in self.Data:
                    Speak("Ok..Redirecting You To Home Screen")
                    press_and_release('windows + m')

                elif "Jarvis" in self.Data or "jarvis" in self.Data or "javed" in self.Data or "jarves" in self.Data or "religious" in self.Data or "Jarvis" in self.Data or "jar" in self.Data:
                    ("Yes Sir! What can i do for you")

                elif 'youtube' in self.Data:
                    Speak("what you will like to watch ?")
                    qrry = MicExecution().lower()
                    kit.playonyt(f"{qrry}")

                elif 'search on youtube' in self.Data:
                    self.Data = self.Data.replace("search on youtube", "")
                    webbrowser.open(f"www.youtube.com/results?search_query={self.Data}")

                elif 'close chrome' in self.Data:
                    os.system("taskkill /f /im chrome.exe")
                    Speak("Chrome has been closed")

                elif 'close youtube' in self.Data:
                    os.system("taskkill /f /im msedge.exe")

                elif 'the time' in self.Data or 'what time is it' in self.Data or 'what date is it today' in self.Data:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    Speak(f"Sir, the time is {strTime}")

                elif 'the date' in self.Data or 'what date is today' in self.Data or 'what is the date today' in self.Data:
                    strDate = datetime.datetime.now().strftime("%d %B %Y")
                    Speak(f"Sir, today's date is {strDate}")

                elif 'the day' in self.Data or 'what day is it today' in self.Data or 'what is the day today' in self.Data:
                    today = datetime.datetime.now().strftime("%A")
                    Speak(f"Sir, today is {today}")
                
                elif "close command prompt" in self.Data:
                    os.system("taskkill /f /im cmd.exe")

                elif "shut down the system" in self.Data:
                    os.system("shutdown /s /t 5")

                elif "restart the system" in self.Data:
                    os.system("shutdown /r /t 5")

                elif "Lock the system" in self.Data:
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

                elif 'google god mode' in self.Data:
                    Speak("what should I search ?")
                    qry = MicExecution().lower()
                    webbrowser.open(f"{qry}")

                elif "take screenshot" in self.Data:
                    Speak('tell me a name for the file')
                    name = MicExecution().lower()
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    Speak("screenshot saved")

                elif "volume up" in self.Data or "increase the volume" in self.Data:
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

                elif "volume down" in self.Data or "decrease the volume" in self.Data:
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

                elif "mute" in self.Data:
                    pyautogui.press("volumemute")

                elif "scroll down" in self.Data:
                    pyautogui.scroll(1000)

                elif 'type' in self.Data: #10
                    self.Data = self.Data.replace("type", "")
                    pyautogui.write(f"{self.Data}")

                elif 'close the window' in self.Data:
                    pyautogui.hotkey('ctrl', 'shift', 'w')

                elif 'good bye jarvis' in self.Data or 'goodbye jarvis' in self.Data or 'good bye jarvis' in self.Data:
                    Speak("Ok Sir, Bye")
                    playsound("C:\\Users\\HP\\Desktop\\JARVIS-ChatGPT-main (Github)\\Assistant\\sounds\\sleep.mp3")
                    break

                else:                    
                    Reply = ReplyBrain(self.Data)
                    Speak(Reply)

#########################################################################################################

startExecution = MainThread

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_mainGUIfile() 
        self.jarvis_ui.setupUi(self)
        self.jarvis_ui.pushButton_Start.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_Exit.clicked.connect(self.close)
    
    def startFunc(self):
        self.jarvis_ui.movies = QtGui.QMovie("C:/Users/HP/Downloads/008c1ec6621b132d42af32394fde1611.gif")
        self.jarvis_ui.label.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000) #if needed you can change this.
        startExecution.start()

    def showtime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate) 
        label_day = current_date.toString("dddd")
        self.jarvis_ui.text_Time.setText(label_time)
        self.jarvis_ui.text_Date.setText(label_date)
        self.jarvis_ui.text_Day.setText(label_day)

Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())

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
                MainThread(QThread)()

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

# ---------------------------------------------------------------------------------------------------------------

