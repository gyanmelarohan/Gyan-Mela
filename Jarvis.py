import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import time
from bs4 import BeautifulSoup
#import PyPDF2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 195)


# text to speech


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=7)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    query.lower()
    return query


def take_wish():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak(" ")
        return "none"
    query.lower()
    return query


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=80567b540e3049e5b890338fe70b8716'

    main_page = requests.get(main_url).json()

    articles = main_page["articles"]

    head = []

    day = ["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])

    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

# to whish


def pdf_reader():
    pass


def wish_me():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
        speak(f"Good Morning Sir, its {tt}")

    elif hour >= 12 and hour <= 18:
        speak(f"Good Afternoon Sir, its {tt}")
    else:
        speak(f"Good Evening Sir, its {tt}")

    speak("i am jarvis sir, please tell me how may i help you sir")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('1012.shreyas@gmail.com', 'B$$hr3y@$')
    server.sendmail('1012shreyas@gmail.com', to, content)
    server.close()


def Task_Execution():

    #just checking if its you

    speak("Verified user, Verification Successful")

    #complements
    speak("Welcome back shreyas sir")
    wish_me()


    while True:
        query = take_command().lower()

        # defining tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            speak("Opening Notepad")

        #elif "how to do mode" in query:
            #from pywikihow import search_wikihow
            #speak("sir, how to do mode is activated")
            #while True:
                #speak("please tell me what you want to know")
                #how = take_command()
                #try:
                    #if "exit" in how or "close" in how:
                        #speak("ok sir, how to do mode is closed")
                        #break
                    #else:
                        #max_results = 1
                        #how_To = search_wikihow(how, max_results)
                        #assert len(how_To) == 1
                        #speak(how_To[0].summary)

                #except Exception as e:
                    #speak("sorry sir, i am not able to find this one")

        elif "calculator" in query:
            cpath = "C:\\Users\\1012s\\Desktop\\Calculator.exe"
            os.startfile(cpath)
            speak("opening calculator")
            time.sleep(10)

        elif "pdf" in query:
            pdf_reader()

        elif "close notepad" in query:
            speak('Okay sir, closing Notepad')
            os.system("taskkill /f /im notepad.exe")

        elif "calculations" in query:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Sir, What should i calculate, Example: 3 plus 3")
                    print("listening...")
                    r.adjust_for_ambient_noise(source)

                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op):
                    import operator
                    return{
                        '+': operator.add,
                        '-': operator.sub,
                        'X': operator.mul,
                        'x': operator.mul,
                        '/': operator.__truediv__,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("sir, your result is")
                speak(eval_binary_expr(*(my_string.split())))

            except Exception as e:
                print(e)
                speak("sir, i am not able to do this one due to an error")

        elif "open teams" in query:
            mpath = "C:\\ProgramData\\1012s\\Microsoft\\Teams\\Update.exe"
            speak('Opening MS Teams')
            os.startfile(mpath)

        elif "volume up" in query:
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

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "sms" in query:
            speak("sir,what should i say")
            msz = take_command()

            from twilio.rest import Client

            # Find your Account SID and Auth Token at twilio.com/console
            # and set the environment variables. See http://twil.io/secure
            account_sid = 'AC444e2ea5ebd19e33cd04b47e9bc2dd51'
            auth_token = '4bb017c4738d32a2a62e2027547f19ab'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body=msz,
                    from_='+17206152758',
                    to='+919483868411'
                )

            print(message.sid)

            speak(
                "sir,i would like to say you that i am going to terminate after every call")

        elif "call" in query:
            speak("sir,what should i say")
            msz = take_command()

            from twilio.rest import Client

            # Find your Account SID and Auth Token at twilio.com/console
            # and set the environment variables. See http://twil.io/secure
            account_sid = 'AC444e2ea5ebd19e33cd04b47e9bc2dd51'
            auth_token = '4bb017c4738d32a2a62e2027547f19ab'
            client = Client(account_sid, auth_token)

            message = client.calls \
                .create(
                    twiml='this is a testing messagee from jarvis',
                    from_='+17206152758',
                    to='+919483868411'
                )

            print(message.sid)

        elif "temperature" in query:
            speak("which city temperature should i search sir")
            city = take_command()
            search = f"temperature in {city}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "open command prompt" in query:
            speak('Opening CMD')
            os.system("start cmd")

        elif "close command prompt" in query:
            speak('Okay sir, closing command prompt')
            os.system("taskkill /f /im cmd.exe")

        elif "open camera" in query:
            cam = cv2.VideoCapture(0)
            while True:
                ret, img = cam.read()
                cv2.imshow('Web Camera', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cam.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\1012s\\Desktop\\Jarvis\\Songs"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif "what can you do" in query:
            speak("sir i can do the following things:")
            speak("open apps")
            speak("control volume")
            speak("do a sms or a call")
            speak("can say temperature annd where we are")
            speak("set alarm")
            speak("shutdown, restart or sleep the system")
            speak("open websites like youtube, bing")
            speak("open wikipedia")
            speak("search online in bing")
            speak("send messages in whatsap")
            speak("tell jokes and news")

        elif "set alarm" in query:
            music_dir = "C:\\Users\\1012s\\Desktop\\Jarvis\\Songs"
            songs = os.listdir(music_dir)
            current_hour = int(datetime.datetime.now().hour)
            current_min = int(datetime.datetime.now().minute)
            speak('What hour should i set, sir')
            timer_hour = int(take_command())
            speak('What minute should i set sir')
            timer_min = int(take_command())
            speak('Timer has been set sir')
            take_command()
            # time.sleep(50)
            if current_hour == timer_hour and current_min == timer_min:
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("Sir,wake up")
            take_command()

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            speak(results)
            time.sleep(20)

        elif "open youtube" in query:
            speak('Opening youtube')
            webbrowser.open("youtube.com")

        elif "open scratch games" in query:
            speak('Opening scratch games')
            webbrowser.open("scratch.mit.edu")

        elif "open stackoverflow" in query:
            speak('Opening Stackoverflow')
            webbrowser.open("stackoverflow.com")

        elif "online teams" in query:
            speak('opening teams')
            webbrowser.open("teams.microsoft.com")

        elif "open bing" in query:
            speak("Sir, What should i search on bing")
            cm = take_command().lower()
            webbrowser.open(f"{cm}")
            time.sleep(20)

        elif "send message" in query:
            speak("Sir what message should i send")
            msg = take_command().lower()
            current_hour = int(datetime.datetime.now().hour)
            current_min = int(datetime.datetime.now().minute + 0.50)
            kit.sendwhatmsg("+919482227048",
                            f"{msg}", current_hour, current_min)
            time.sleep(20)

        elif "play song" in query:
            speak('Playing Song')
            kit.playonyt(
                "99 | New Audio Jukebox 2019 | Ganesh| Bhavana| Arjun Janya| Preetham Gubbi| Kaviraj | Ramu Films")
            time.sleep(20)

        elif "send email" in query:
            try:
                speak("What should i say?")
                content = take_command().lower()
                to = "1012.shreyas@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to shreyas")

            except Exception as e:
                print(e)
                speak('Sorry sir i am not able to send email to shreyas')

        elif "tell me some jokes" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()

        elif "where am i" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requeets = requests.get(url)
                geo_data = geo_requeets.json()

                city = geo_data['city']

                country = geo_data['country']

                speak(f"Sir, we are in {city} city of {country} country")
            except Exception as e:
                speak(
                    "Sorry sir, due to net issues i am not able to find our location")

        elif "take screenshot" in query:
            speak("Sir, please tell me the name for this file")
            name = take_command().lower()
            speak("Please hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("sir the screenshot has been taken and saved in the folder")

        elif "battery" in query or "power" in query:
            import psutil
            battery = psutil.sensors_battery()
            persentage = battery.percent
            speak(f"sir our system has {persentage} percent battery left")

            if persentage <= 60:
                speak("sir we are good to go")

            if persentage <= 30 and persentage >= 60:
                speak(
                    "sir, it would be better if we would put our system to charge")

            if persentage <= 20:
                speak(
                    "sir, the state is crtical, we should put our system to charge right away")

        elif "hello" in query:
            speak("hello sir, may i help you with something")

        elif "how are you" in query:
            
            speak("i am fine sir, what about you")

        elif "i am good" in query:
            speak("that's great sir")

        elif "thank you" in query:
            speak("it's my pleasure sir")

        elif "rest" in query:
            speak("okay sir, i am always there for you sir")
            break


        #saying this after every command
        speak(" what else can i do for you sir ")



#Where the whole code runs

def main():
    if __name__ == "__main__":
        while True:
            #permission = take_command()
            #if "wake up" in permission:
            Task_Execution()
            #elif "sleep" in permission:
                #speak('thanks for using me sir, have a good day')
                #sys.exit()


#calling the main function
main()

