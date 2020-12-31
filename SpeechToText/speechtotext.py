import time
from recordaudio import recordvoice
from predict import predict_audio   
def speech2text():
    audio=recordvoice()
    query=predict_audio(audio)
    # if query !="None":
    time.sleep(0.5)
    return query
            
if __name__ == '__main__':
	speech2text()