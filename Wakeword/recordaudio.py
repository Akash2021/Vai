def recordvoice():
	import speech_recognition as sr
	r = sr.Recognizer()
	r.energy_threshold=500
	with sr.Microphone() as source:
		print("Listening...")
        # r.pause_threshold = 1
		audio = r.listen(source)
	return audio
