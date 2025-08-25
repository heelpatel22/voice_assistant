import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyaudio

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            return command.lower()
        except:
            return " "
        
while True:
    command = take_command()
    if "time" in command:
        speak(datetime.datetime.now().strftime("%H:%M:%S"))
    elif "google" in command:
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "youtube" in command:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif "stop" in command:
        speak("Goodbye")
        break