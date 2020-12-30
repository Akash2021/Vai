import time
from record_audio import record_voice
from predict import predict_audio
def detect_wakeword():
    while True:
        time.sleep(0.01)
        audio=record_voice()
        if predict_audio(audio)== "happy":
            print("wakeword detected")
            time.sleep(0.2)
            return True
#            break


#print(detect_wakeword())
