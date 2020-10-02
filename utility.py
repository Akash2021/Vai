import wikipedia
import webbrowser
import os
import pyttsx3
import datetime
engine = pyttsx3.init();

def speak(audio):
	engine.say(audio) 
	engine.runAndWait()

def takeCommand():
    """It takes microphone input from the user and returns string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def wishme():
	 hour = int(datetime.datetime.now().hour)
	 if hour>=0 and hour <12:
	 	speak("Good Morning!")

	 elif hour>=12 and hour <18:
	 	speak("Good Afternoon")

	 else :
	 	speak("Good Evening!")
def openn(query):
    
	webbrowser.open(f'{query}.com')