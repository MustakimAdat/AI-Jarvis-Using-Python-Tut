
import pywhatkit # pip install pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow # pip install pywikihow
import os
import speech_recognition as sr
import webbrowser as web
import bs4
import pyttsx3
from time import sleep
import requests
import wolframalpha # pip install wolframalpha
import datetime
import time
import playsound
import json
import socket
import urllib.request
from playsound import playsound
from pyautogui import click
from keyboard import write

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

def DownloadYouTube():
    from pytube import YouTube #pip install pytube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=942,y=59)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download('C:\\Users\\HP\\Videos\\Youtube Video Downloads\\')


    Download(Link)


    Speak("Done Sir , I Have Downloaded The Video .")

    Speak("You Can Go And Check It Out.")


    os.startfile('C:\\Users\\HP\\Videos\\Youtube Video Downloads\\')

def SpeedTest():

    os.startfile("C:\\Users\\HP\\Desktop\\AI Jarvis Using Python Tut\\DataBase\\Gui Programs\\SpeedTestGui.py")

def WolfRam(query):

    api_key = "8EET2X-UTJWVUUU28"

    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)


    try:

        Answer = next(requested.results).text

        return Answer

    except:

        Speak("A String Value Is Not Answerable .")

def Calculator(query):

    Term = str(query)

    Term = Term.replace("jarvis","")
    Term = Term.replace("into","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("into","*")
    Term = Term.replace("by","/")

    Final = str(Term)

    try:

        result = WolfRam(Final)
        Speak(F"{result}")

    except:

        Speak("A String Value Is Not Answerable .")

def Temp(query):

    Term = str(query)

    Term = Term.replace("jarvis ","")
    Term = Term.replace("in ","")
    Term = Term.replace("what is the ","")
    Term = Term.replace("temperature ","")
    Term = Term.replace("what's ","")

    temp_query = str(Term)

    if 'outside' in temp_query:

        var1 = "Temperature in Hyderabad"

        answer = WolfRam(var1)

        Speak(f"{var1} Is {answer}")

    else:

        var2 = "Temperature In " + temp_query

        answ = WolfRam(var2)

        Speak(f"{var2} Is {answ}")

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

def My_Location():

    # Get public IP address
    ip_address = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    # Get location information using IP address
    url = f'http://ipinfo.io/{ip_address}/json'
    response = urllib.request.urlopen(url)
    data = json.load(response)
    # Extract location information
    city = data['city']
    region = data['region']
    country = data['country']
    loc = data['loc']
    latitude, longitude = loc.split(',')
    # Speak the location information
    Speak(f"Sir, You are currently located in {city}, {region}, {country}.")
    Speak(f"Your current coordinates are latitude {latitude} and longitude {longitude}.")

def CoronaVirus(Country):

    countries = str(Country).replace(" ","")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_ = 'maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    cases , Death , recovored = Data

    Speak(f"Cases : {cases}")
    Speak(f"Deaths : {Death}")
    Speak(f"Recovered : {recovored}")

def set_alarm():
    Speak("What time should I set the alarm for? (Format: HH:MM AM/PM).")
    alarm_time = input()
    Speak("Alarm set for " + alarm_time + ".")

    # split the input time into hours, minutes and am/pm
    alarm_time_list = alarm_time.split()
    hours, minutes = map(int, alarm_time_list[0].split(":"))
    am_pm = alarm_time_list[1]

    # adjust hours for PM times
    if am_pm.lower() == "pm" and hours != 12:
        hours += 12
    
    # set the alarm time
    alarm_time = datetime.time(hour=hours, minute=minutes)
    
    # get current time
    current_time = datetime.datetime.now().time()
    
    # check if the alarm time is in the future
    while alarm_time > current_time:
        time.sleep(1)
        current_time = datetime.datetime.now().time()

    # play the alarm sound
    Speak("Wake up! It's time!")
    playsound('C:\\Users\\HP\\Desktop\\AI Jarvis Using Python Tut\\DataBase\\Sounds\\1.mp3')

    # listen for "I woke up"
    while True:
        Speak("Did you wake up?")
        response = TakeCommand()
        if "yes" in response.lower() or "woke up" in response.lower():
            Speak("Good job! Alarm stopped.")
            break
        else:
            Speak("I'll ask again in some time.")
            time.sleep(10)
            


