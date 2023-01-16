import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import time
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 180)

# to convert voice into text
def speak(audio):
    global y
    y = print(audio)
    print(y)
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=7)

    try:
        speak("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        speak(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return ""
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


def Task_Execution():

    wish_me()
    if 1:
        x = speak(" I am an AI")
        x = speak ("I will help you in your journey to learn Ancient languages")
        x = speak("would you like to see a video about ancient languages")
    while True:
        
        query = take_command().lower()

        # defining taskd
        

        if "video" in query or "yes" in query or "yash" in query:
            speak('Playing the video')
            kit.playonyt(
                "Top 10 Oldest Languages in The World | Ancient Languages used Today | info Planet")
            time.sleep(535)




        if "what can you do" in query:
            speak("sir/mam i can do the following things:")
            speak("I can play you a video about ancient languages")
            speak("I can give you info on ancient languages")


        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            
            speak("according to wikipedia")
            speak(results)
            time.sleep(20)

        elif "ancient languages" in query or "patient languages" in query or "in cient languages" in query:
            results = wikipedia.summary("ancient languages", sentences=5)


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
if __name__ == "__main__":
    while True:
        Task_Execution()
        



