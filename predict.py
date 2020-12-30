import deepspeech
import wave
import numpy as np
from pydub import AudioSegment as am

def predict_audio(audio):
	import speech_recognition as sr
	r = sr.Recognizer()
	try:
		print("Recognizing...")    
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n")  #User query will be printed.

	except Exception as e:
        # print(e)    
		print("Say that again please...")   #Say that again will be printed in case of improper voice 
		return "None" #None string will be returned
	print(query)
	return query


def predicts_audio(audio):
	w = wave.open(audio, 'r')
	sound = am.from_file(audio, format='wav', frame_rate=w.getframerate())
	sound = sound.set_frame_rate(16000)
	sound.export('1', format='wav')
	w = wave.open('1', 'r')
	model = deepspeech.Model("deepspeech-0.9.1-models.pbmm") 
	# model.enableExternalScorer('deepspeech-0.9.1-models.scorer.1') # scorrer file here using it might make your application slow
	frames = w.getnframes()
	buffer = w.readframes(frames)
	data16 = np.frombuffer(buffer, dtype=np.int16)
	text = model.stt(data16)
	print(text)

if __name__ == '__main__':
	predicts_audio('arctic_a0001.wav')
