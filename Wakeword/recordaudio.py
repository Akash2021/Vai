def recordvoice():
	import speech_recognition as sr
	r = sr.Recognizer()
	r.energy_threshold=500
	with sr.Microphone() as source:
		print("Listening...")
	# r.pause_threshold = 1
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	return audio
