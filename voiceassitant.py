import speech_recognition as sr
import pyttsx3
import datetime as dt
import webbrowser as wb
import os
import subprocess


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 160)

def open_app(name):
    name = name.lower()

    
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "vs code": r"C:\Users\<your-username>\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
    }

    if name in apps:
        try:
            subprocess.Popen(apps[name])
            speak(f"Opening {name}")
        except Exception as e:
            speak(f"Sorry, I couldn't open {name}.")
    else:
        speak(f"App {name} not recognized.")
    

def wish_user():

    hour = dt.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you?")

def take_command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = rec.listen(source)

    try:
        print("Recognizing...")
        command = rec.recognize_google(audio)
        print(f"You said: {command}")
    except Exception:
        speak("Sorry, I didn't catch that.Can you speak again?")
        return ""
    return command.lower()

def run():
    wish_user()
    while True:
        command = take_command()

        if "hello" in command:
            speak("Hello! Great to hear you. How are you?")
        elif " about you" in command or "who are you" in command:
            speak("I am your voice assistant ")
        elif "what is your name" in command or "kya naam " in command:
            speak("my name is Paradox")
        elif "how are you" in command:
            speak("I am fine! ")
        elif "help me" in command or "madad" in command:
            speak("i can help you ")
        elif "time" in command:
            time = dt.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")
            print(f"The time is {time}")
        elif "date" in command:
            date = dt.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {date}")
            print(f"Today's date is {date}")
        elif "search" in command:
            speak("What should I search for?")
            query = take_command()
            url = f"https://www.google.com/search?q={query}"
            wb.open(url)
            speak(f"Searching for {query}")
        elif "open" in command:
           app = command.replace("can you open ", "").strip()
           open_app(app)
        elif "exit" in command or "stop" in command or "bye" in command:
            speak("OKAY Goodbye Have a nice day!")
            break
        else :
            speak("soorry i am not an advanced voice assistant")
            


run()
