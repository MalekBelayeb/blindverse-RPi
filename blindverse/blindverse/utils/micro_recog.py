import speech_recognition as sr
from blindverse.utils.consts import DURATION_OF_THE_QUESTION

r = sr.Recognizer()
def record():
    try:
        with sr.Microphone() as source:
            print('running')
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio_data = r.record(source, duration=DURATION_OF_THE_QUESTION)
            
            my_text = r.recognize_google(audio_data)
            my_text = my_text.lower()
            print(my_text)
            return my_text
            
    except sr.RequestError as e:
        print('error {0}'.format(e))
        
    except sr.UnknownValueError:
        print('error 2')

