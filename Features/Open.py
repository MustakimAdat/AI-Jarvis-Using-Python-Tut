import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def OpenExe(Query):
    Query = str(Query).lower()

    if "jarvis" in Query:
        if "visit" in Query:
            Nameofweb = Query.replace("visit ","")
            Link = f"https://www.{Nameofweb}.com"
            webbrowser.open(Link)
            return True

        elif "launch" in Query:
            Nameofweb = Query.replace("launch ","")
            Link = f"https://www.{Nameofweb}.com"
            webbrowser.open(Link)
            return True

        elif "open" in Query:
            Nameoftheapp = Query.replace("open ","")
            Nameoftheapp = Query.replace("jarvis ","")
            Nameoftheapp = Query.replace("jarved ","")
            Nameoftheapp = Query.replace("Jarvis ","")
            Nameoftheapp = Query.replace("Religious ","")
            Nameoftheapp = Query.replace("religious ","")

            if "youtube" in Nameoftheapp:
                pass      
            
            pyautogui.press('win')
            sleep(1)
            keyboard.write(Nameoftheapp)
            sleep(1)
            keyboard.press('enter')
            sleep(0.5)  
            return True

        elif "start" in Query:
            Nameoftheapp = Query.replace("open ","")

            if "chrome" in Nameoftheapp:
                os.startfile(r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                return True

            elif "youtube" in Nameoftheapp:
                pass

    else:
        return False
