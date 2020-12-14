def predict_audio(audio):
	import speech_recognition as sr
	r = sr.Recognizer()
	try:
#		print("Recognizing...")    
		query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
#		print(f"User said: {query}\n")  #User query will be printed.

	except Exception as e:
        # print(e)    
		print("Say that again please...")   #Say that again will be printed in case of improper voice 
		return "None" #None string will be returned
	print(query)
	return query


def infrence(sample):
  waveform, sample_rate =librosa.load(sample,sr=16000)
  print(waveform.shape)
  waveform,index=librosa.effects.trim(waveform)
  print(waveform.shape)
  waveform=librosa.util.fix_length(waveform, 16000, mode='constant')
  waveform=np.transpose(waveform)
  waveform=np.expand_dims(waveform, axis=0)
  waveform=torch.from_numpy(waveform)
  spectogram=torchaudio.transforms.MelSpectrogram()(waveform)
  spectogram=torch.unsqueeze(spectogram,0)
  outputs = net(spectogram)
  _, predicted = torch.max(outputs.data, 1)
  print(predicted)
