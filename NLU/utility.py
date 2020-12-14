import wikipedia
import webbrowser
import os
import pyttsx3
import datetime
from jaro import jaro_Winkler
import string
from Search import search
from google_search import searchh
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))
en_stops.add("please")
engine = pyttsx3.init();

file1 = open("websitelist.txt","r") 
uname=""

def wishme():
     print("hello")
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour <12:
        if uname=="":
            speak("Good Morning!")
        else:
            speak(f'Good Morning {uname}')
     elif hour>=12 and hour <18:
        if uname=="":
            speak("Good Afternoon")
        else:
            speak(f'Good Afternoon {uname}')

     else :
        if uname=="":
            speak("Good Evening!")
        else:
            speak(f'Good Evening! {uname}')

def setusername():
    speak("What should i call you ")
    global uname
    uname = takeCommand()
    speak(f'Your name is set to {uname}' ) 
    speak(f'Do you want to change it?')
    command=takeCommand()
    if command=="yes" or command=="yeah" :
        setusername()
        
def preprocess(query):
    query=query.lower()
    query=query.split("open",1)[1] 
    query=query.translate(str.maketrans('', '', string.punctuation)) # remove punctuations 
    query= query.split()
    s=""
    for word in query:
        if word not in en_stops:
            s+=word

    return s
    
def find(s1):
    ma=float(0.0)
    ans=""
    for x in file1.readlines():
        temp=jaro_Winkler(s1,x)
        if temp>ma and temp>0.55:
            ans=x
            ma=temp
    return ans

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

def openn(query):
    query=(find(preprocess(query)))
    webbrowser.open(f'{query}')
    return f'opening {query}'

def time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f" the time is {strTime}")
    print(f"the time is {strTime}")

def searching(query):
    return searchh(query)
