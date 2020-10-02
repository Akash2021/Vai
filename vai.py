import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
engine = pyttsx3.init();
def speak(audio):
	engine.say(audio) 
	engine.runAndWait()

def wishme():
	 hour = int(datetime.datetime.now().hour)
	 if hour>=0 and hour <12:
	 	speak("Good Morning!")

	 elif hour>=12 and hour <18:
	 	speak("Good Afternoon")

	 else :
	 	speak("Good Evening!")
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

if __name__ == "__main__":
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case
        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The, time is {strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
 

