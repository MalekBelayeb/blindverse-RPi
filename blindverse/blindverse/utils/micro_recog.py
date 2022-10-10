import speech_recognition as sr
import sys
sys.path.append('/home/pi/Desktop/blindverse-RPi/blindverse')
from blindverse.utils.consts import DURATION_OF_THE_QUESTION
from blindverse.utils.audio_config import string_to_speech
from blindverse.utils.strings import *

r = sr.Recognizer()

def record():
    string_to_speech(start_recording ,lang = get_lang())
    try:
        with sr.Microphone(device_index=0) as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio_data = r.record(source, duration=DURATION_OF_THE_QUESTION)
            my_text = r.recognize_google(audio_data)
            my_text = my_text.lower()
            return my_text
    except sr.RequestError as e:
        print('Error {0}'.format(e))
    except sr.UnknownValueError:
        print('Error 2 try again')


