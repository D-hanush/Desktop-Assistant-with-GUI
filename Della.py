import speech_recognition as sr
import os
import webbrowser
import sys
import datetime
import pyttsx3
import pyjokes
import wikipedia
import pywhatkit as kit
import requests
from bs4 import BeautifulSoup
import pyautogui
from twilio.rest import Client
from newsapi import NewsApiClient
from pywikihow import search_wikihow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow, QApplication
from MYui import Ui_Myui

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Della. Please tell me how may I help you.")

class MainThread(QThread):
    update_ui_signal = pyqtSignal(str)
    close_app_signal = pyqtSignal()

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

    def get_news(self, api_key):
        newsapi = NewsApiClient(api_key=api_key)
        top_headlines = newsapi.get_top_headlines(language='en', country='us')
        if top_headlines['status'] == 'ok':
            articles = top_headlines['articles']
            headlines = [article['title'] for article in articles[:5]]
            print("Here are the latest news headlines:")
            for i, headline in enumerate(headlines, 1):
                print(f"{i}. {headline}")
                speak(f"{i}. {headline}")
        else:
            speak("Sorry, I couldn't fetch the news at the moment.")

    def PlayYoutube(self, query):
        search_term = query.replace("play ", "").replace(" on youtube", "")
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)

    def TaskExecution(self):
        wishMe()
        while True:
            query = self.takeCommand().lower()

            if "tell me about" in query or "Who is" in query:
                topic = query.replace("tell me about", "").strip()
                url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
                r = requests.get(url)
                summary = r.json().get('extract', 'Sorry, I could not find any information on that topic.')
                speak(summary)
                print(summary)

            elif 'your name' in query:
                speak("My name is Della")

            elif 'laugh' in query or 'smile' in query:
                speak("ha ha ha hah ha ha")

            elif "hello" in query or "hey della" in query:
                speak("Hello sir")

            elif "how are you della" in query or "how r u" in query:
                speak("I am fine sir, how about you")

            elif "i am fine" in query:
                speak("Okay sir")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

            elif 'the date' in query:
                strDate = datetime.datetime.now().strftime("%Y-%m-%d")
                print(f"Todays date is {strDate}")
                speak(f"Today's date is {strDate}")

            elif 'play' in query:
                self.PlayYoutube(query)

            elif "volume up" in query:
                pyautogui.press("volumeup")

            elif "volume down" in query:
                pyautogui.press("volumedown")

            elif "volume mute" in query or "mute" in query:
                pyautogui.press("volumemute")

            elif "news" in query:
                api_key = '1***************************4' #Add your api_key 
                self.get_news(api_key)

            elif 'open' in query:
                speak(f"opening {query}")
                website = query.replace('open ', '')
                webbrowser.open(f"https://www.{website}.com")

            elif 'take me to whatsapp' in query:
                speak("oky opening whatsapp")
                webbrowser.open("https://web.whatsapp.com")

            elif 'finish' in query or 'close' in query or 'tab' in query:
                pyautogui.hotkey("ctrl", "w")
                speak("Closing tab")

            elif 'joke' in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "send message" in query:
                print("Sir what should i send in message")
                speak("Sir what should i send in message")
                msz = self.takeCommand()

                account_sid = 'A************************4' #Add your account_sid
                auth_token = 'b************************c' #Add your auth_token

                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body=msz,
                    from_='+13312444914',
                    to='+91*********7' #add your number
                )

                print(f"Message sent with SID {message.sid}")
                speak(f"Message sent with SID {message.sid}")

            elif "make a call" in query:
                speak("Making Call ")
                account_sid = 'A***************************4' #Add your account_sid
                auth_token = 'b**************************c' #Add your auth_token

                client = Client(account_sid, auth_token)

                message = client.calls.create(
                    twiml='<Response><Say>This is the second message from  Della..</Say></Response>',
                    from_='+13312444914',
                    to='+91**********1' Add your number
                )

            elif "my ip address" in query:
                ip = requests.get('https://api.ipify.org').text
                print(f"Your IP address is {ip}")
                speak(f"Your IP address is {ip}")

            elif "temperature" in query:
                search = query
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                print(f"Current {search} is {temp}")
                speak(f"Current {search} is {temp}")

            elif "activate mode" in query:
                speak("How-to mode is activated")
                while True:
                    speak("Please tell me what you want to know")
                    how = self.takeCommand()
                    try:
                        if "exit" in how or "quit" in how:
                            speak("Okay, how-to mode is closed")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("Sorry, I am unable to find this")

            elif "no thanks" in query:
                speak("Thanks For Using Me Have A Nice Day")
                print("Thanks For Using Me Have A Nice Day")
                self.close_app_signal.emit()
                sys.exit()

            speak("Is there anything else I can help you with?")


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Myui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        startExecution.update_ui_signal.connect(self.updateUI)
        startExecution.close_app_signal.connect(self.close_app)

    def startTask(self):
        self.ui.movie = QMovie("C:/Users/HP/Music/DellaGUI\Loading.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

    def updateUI(self, message):
        self.ui.label.setText(message)

    def close_app(self):
        self.close()

app = QApplication(sys.argv)
Della = Main()
Della.show()
sys.exit(app.exec_())



