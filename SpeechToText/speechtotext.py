import time
from recordaudio import recordvoice
from predict import *   
import warnings
warnings.filterwarnings("ignore")
def speech2text():
    audio=recordvoice()
    with open('speech.wav','wb') as f:
    	f.write(audio.get_wav_data())
    query=predicts_audio('speech.wav')
    # if query !="None":
#    print('h1'+query)
    return query
            
if __name__ == '__main__':
	speech2text()
