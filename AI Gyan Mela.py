
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import time
import pywhatkit as kit
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer,Qt,QTime
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from GUI import Ui_Gyan_Mela_GUI
import sys
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 180)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

# to convert voice into text




def take_wish():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        sr.pause_threshold = 1
        audio = sr.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("recognizing...")
        query = sr.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again pls")
    query.lower()
    return query

def wish_me():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
        speak(f"Good Morning Sir/Mam, its {tt}")

    elif hour >= 12 and hour <= 16:
        speak(f"Good Afternoon Sir/Mam, its {tt}")
    else:
        speak(f"Good Evening Sir/Mam, its {tt}")

class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run (self):
        self.Task_Execution()

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            self.audio = r.listen(source, timeout=10, phrase_time_limit=7)

        try:
            print("recognizing...")
            self.query = r.recognize_google(self.audio, language='en-in')
            print(f"user said: {self.query}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        self.query
        return self.query

    def Task_Execution(self):
        wish_me()
        speak("before we start with our project,we would like to give you a demo presentaion")
        os.startfile("D:\\7A B.S.Shreyas\Gyan Mela\\Computer gyan mela ai ppt 1.pptx")

        if 1:
            self.x = speak("would you like to see a video about ancient languages, if yes please say 'play the video'")

        while True:
            self.query = self.take_command().lower()

            # defining 
            
            if "video" in self.query:
                speak('Playing the video')
                kit.playonyt("Top 10 Oldest Languages in The World | Ancient Languages used Today | info Planet")
                time.sleep(535)

            elif "gyan mela" in self.query or "gyanmela" in self.query:
                speak("Gyan mela is a exhibition of knowledge made by the children of New Horizon Gurukul")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

            elif "what can you do" in self.query:
                speak("sir/mam i can do the following things:")
                speak("I can play you a vedio about ancient languages")
                speak("I can give you info on ancient languages")


            elif "wikipedia" in self.query:
                speak("Searching Wikipedia...")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=3)
                    
                speak("according to wikipedia")
                speak(results)
                time.sleep(20)

            elif "hello" in self.query:
                speak("hello sir, may i help you with something")

            elif "how are you" in self.query:
                    
                speak("i am fine sir, what about you")

            elif "i am good" in self.query:
                speak("that's great sir")

            elif "thank you" in self.query:
                speak("it's my pleasure sir")

            elif "rest" in self.query:
                speak("okay sir, i am always there for you sir")



                #saying this after every command
            speak(" what else can i do for you sir ")


punnerr = MainThread()
class Main(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.ui = Ui_Gyan_Mela_GUI()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Media/gif.gif")
        self.ui.movie1 = QtGui.QMovie("Media/gif3.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.label_2.setMovie(self.ui.movie1)
        self.ui.movie.start()
        self.ui.movie1.start()
        #self.ui.label_2.setText(y)
        timer = QTimer(self)
        timer.start (1000)
        punnerr.start()


        
app = QApplication(sys.argv)
AI = Main()
AI.show()
exit(app.exec_())
