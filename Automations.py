from datetime import datetime
from os import startfile
import os
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
# from notifypy import Notify
import pyttsx3
import speech_recognition as sr
from geopy.distance import great_circle # pip install geopy
from geopy.geocoders import Nominatim
import geocoder # pip install geocoder
import webbrowser as web
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def WhatsappMsg(name,message):
     
    startfile("C:\\Users\\HP\\Desktop\\WhatsApp.lnk")

    sleep(5)

    press_and_release('ctrl + f')

    sleep(1)

    write(name)

    sleep(0.5)

    click(x=185, y=183)

    sleep(0.5)

    click(x=633, y=698)

    sleep(0.5)

    write(message)

    press('enter')

def WhatsappCall(name):

    startfile("C:\\Users\\HP\\Desktop\\WhatsApp.lnk")

    sleep(5)

    press_and_release('ctrl + f')

    sleep(1)

    write(name)

    sleep(1)

    click(x=185, y=183)

    sleep(1)

    click(x=633, y=698)

    sleep(1)

    click(x=1247, y=61)

def WhatsappVideoCall(name):

    startfile("C:\\Users\\HP\\Desktop\\WhatsApp.lnk")

    sleep(5)

    press_and_release('ctrl + f')

    sleep(1)

    write(name)

    sleep(1)

    click(x=185, y=183)

    sleep(1)

    click(x=633, y=698)

    sleep(1)

    click(x=1196, y=59)

def WhatsappChat(name):

    startfile("C:\\Users\\HP\\Desktop\\WhatsApp.lnk")

    sleep(5)

    press_and_release('ctrl + f')

    sleep(1)

    write(name)

    sleep(0.5)

    click(x=185, y=183)

    sleep(0.5)

def ChromeAuto(command):

    query = str(command)

    if 'new tab' in query:

        press_and_release('ctrl + t')

    elif 'close tab' in query:

        press_and_release('ctrl + w')

    elif 'new window in browser' in query:

        press_and_release('ctrl + n')

    elif 'history' in query:

        press_and_release('ctrl + h')

    elif 'download' in query:

        press_and_release('ctrl + j')

    elif 'bookmark' in query:

        press_and_release('ctrl + d')

        press('enter')

    elif 'incognito' in query:

        press_and_release('Ctrl + Shift + n')

    elif 'switch tab' in query:

        tab = query.replace("switch tab ", "")
        Tab = tab.replace("to","")
        
        num = Tab

        bb = f'ctrl + {num}'

        press_and_release(bb)

def YouTubeAuto(command):

    query = str(command)

    if 'pause' in query:

        press('space bar')

    elif 'resume' in query:

        press('space bar')

    elif 'full screen' in query:

        press('f')

    elif 'film screen' in query:

        press('t')

    elif 'skip' in query:

        press('l')

    elif 'back' in query:

        press('j')

    elif 'increase speed' in query:

        press_and_release('SHIFT + .')

    elif 'decrease speed' in query:

        press_and_release('SHIFT + ,')

    elif 'previous video' in query:

        press_and_release('SHIFT + p')

    elif 'next video' in query:

        press_and_release('SHIFT + n')
    
    elif 'search in youtube' in query:

        click(x=667, y=146)

        Speak("What To Search Sir ?")

        search = TakeCommand()

        write(search)

        sleep(0.8)

        press('enter')

    elif 'mute' in query:

        press('m')

    elif 'unmute' in query:

        press('m')

    elif 'my channel' in query:

        web.open("https://www.youtube.com/channel/UCyFtY8oOXEY4Y0bN1QYNpug")

    else:
        Speak("No Command Found!")

def WindiowsAuto(command):

    query = str(command)

    if 'home screen' in query:

        press_and_release('windows + m')

    elif 'minimize' in query:

        press_and_release('windows + m')

    elif 'windows' in query:

        press('windows')

    elif 'open setting' in query:

        press_and_release('windows + i')

    elif 'open search' in query:

        press_and_release('windows + s')

    elif 'screen shot' in query:

        press_and_release('windows + SHIFT + s')

    elif 'restore windows' in  query:

        press_and_release('Windows + Shift + M')

    else:
        Speak("Sorry , No Command Found!")

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    web.open(url=Url_Place)

    location = location.raw['address']

    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)


    Speak(target)
    Speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")

def OnlinClass(Subject):

    Speak("Joining The Class Sir .")

    if 'science' in Subject:

        from DataBase.OnlineClasses.Links import Science

        Link = Science()

        web.open(Link)

        sleep(10)

        click(x=412, y=571)

        sleep(1)

        click(x=1011, y=443)

        Speak("Class Joined Sir .")

    elif 'mathematics' in Subject:

        from DataBase.OnlineClasses.Links import Maths

        Link = Maths()

        web.open(Link)

        sleep(10)

        click(x=412, y=571)

        sleep(1)

        click(x=1011, y=443)

        Speak("Class Joined Sir .")

    elif 'social' in Subject:

        from DataBase.OnlineClasses.Links import sst

        Link = sst()

        web.open(Link)

        sleep(10)

        click(x=412, y=571)

        sleep(1)

        click(x=1011, y=443)

        Speak("Class Joined Sir .")

    elif 'hindi' in Subject:

        from DataBase.OnlineClasses.Links import Hindi

        Link = Hindi()

        web.open(Link)

        sleep(10)

        click(x=412, y=571)

        sleep(1)

        click(x=1011, y=443)

        Speak("Class Joined Sir .")

    elif 'english' in Subject:

        from DataBase.OnlineClasses.Links import English

        Link = English()

        web.open(Link)

        sleep(10)

        click(x=412, y=571)

        sleep(1)

        click(x=1011, y=443)

        Speak("Class Joined Sir .")

def Notepad():

    Speak("Tell Me The Query .")
    Speak("I Am Ready To Write .")

    writes = TakeCommand()

    time = datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","-") + "-note.txt"

    with open(filename,"w") as file:

        file.write(writes)

    path_1 = "C:\\Users\\HP\\Desktop\\AI Jarvis Using Python Tut//" + str(filename)

    path_2 = "C:\\Users\\HP\\Desktop\\AI Jarvis Using Python Tut\\DataBase\\NotePad" + str(filename)

    os.rename(path_1,path_2)

    os.startfile(path_2)

def CloseNotepad():

    os.system("TASKKILL /F /im Notepad.exe")

# def TimeTable():

#     Speak("Checking....")

#     from DataBase.TimeTable.TimeTable import Time

#     value = Time()

#     Noti = Notify()

#     Noti.title = "TimeTable"

#     Noti.message = str(value)

#     Noti.send()

#     Speak("AnyThing Else Sir ??")

def send_email():
    Speak("Sure, whom should I send the email to?")
    recipient = TakeCommand() # get recipient's name from user
    if recipient.lower() == "mom" or "mummy" :
        recipient = "punjanialin0@gmail.com" # replace with your mom's email address
    if recipient.lower() == "me" or "myself" :
        recipient = "zenogamingoff@gmail.com" # replace with the email address you want give
    else:
        Speak(f"What is {recipient}'s email address?")
        recipient = TakeCommand() # get recipient's email address from user
    Speak("What should be the subject of the email?")
    subject = TakeCommand() # get subject of the email from user
    Speak("What should be the content of the email?")
    body = TakeCommand() # get body of the email from user

    # set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # log in to the sender's email account
    sender_email = 'zenogamingoff@gmail.com' # replace with your email address
    password = 'Miza.aaryan(99)' # replace with your email password
    server.login(sender_email, password)

    # create the email message
    message = f'Subject: {subject}\n\n{body}'

    # send the email
    server.sendmail(sender_email, recipient, message)

    # log out from the SMTP server
    server.quit()
    Speak("Email sent successfully")

def entertainment():
    Speak("What will you like to watch, Netflix, Prime Video, Youtube, or GodMode. or Spotify.")
    response = TakeCommand()

    if "netflix" in response.lower():
        os.startfile("C:\\Users\\HP\\Desktop\\Netflix - Shortcut.lnk")
        sleep(5)
        click(x=1237, y=55)
        sleep(1)
        Speak("What movie would you like to watch on Netflix?")
        moviename = TakeCommand()
        write(moviename)
        sleep(1)
        click(x=161, y=223)
        sleep(1)
        click(x=676, y=212)
        sleep(1)
        click(x=1259, y=695)
        Speak("Enjoy the movie Sir!")