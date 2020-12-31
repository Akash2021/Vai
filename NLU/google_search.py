import webbrowser
import wikipedia
import requests
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))
en_stops.add("please") 
def searchh(query):
# print(en_stops)
# query=str(input())
	query=query.lower()
	# print(query)
	keyword=""
	for word in query.split():
		# print(word)
		if word not in en_stops:
			keyword+=word
	# print(keyword)
	results=""
	try:
	    results = wikipedia.summary(keyword,sentences=2)
	except wikipedia.exceptions.DisambiguationError as e:
		results = wikipedia.summary(e.options[0])
	except wikipedia.exceptions.PageError as e:
		print("Here is what we found on google")
		webbrowser.open("https://google.co.in/search?q=%s" % keyword)
	except wikipedia.exceptions.HTTPTimeoutError as e:
	    print("check your internet connection and try again") 
	# print(results)
	return results
