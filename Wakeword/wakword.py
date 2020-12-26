import time
from record_audio import record_voice
from predict_wakeword import *
from model_wakeword import *
import torch
import librosa
import warnings
warnings.filterwarnings("ignore")
def detect_wakeword():
    while True:
        time.sleep(0.01)
        audio=record_voice()
        with open('speech.wav','wb') as f:
        	f.write(audio.get_wav_data())
        val=infrence('speech.wav')
        vals=str(val)
        if vals == "tensor([12])" or vals == "tensor([18])" or vals == "tensor([19])":
            print("wakeword detected")
            return True
#            break

if __name__ == '__main__':
	detect_wakeword()
#print(detect_wakeword())
