import pygame
from gtts import gTTS

def playAudio(audio_name):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_name)
    pygame.mixer.music.play()

def string_to_speech(text, lang):
    myobj = gTTS(text=text, lang=lang, slow=False)
    myobj.save("/home/pi/Desktop/blindverse-RPi/blindverse/blindverse/speech.mp3")
    playAudio("/home/pi/Desktop/blindverse-RPi/blindverse/blindverse/speech.mp3")


