import wikipedia
import webbrowser
import os
import datetime
from jaro import jaro_Winkler
import string
from Search import search
from google_search import searchh
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))
en_stops.add("please")

file1 = open("websitelist.txt","r") 
uname=""


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
