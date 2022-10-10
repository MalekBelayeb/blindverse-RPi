import sys
sys.path.append('/home/pi/Desktop/blindverse-RPi/blindverse')
from blindverse.utils.strings import *
from blindverse.settings.settings import get_lang
from blindverse.utils.audio_config import string_to_speech

string_to_speech(welcome_text,lang=get_lang())
print(welcome_text)
import time
from barcode_recognition.barcode import execute_barcode_recognition
from money_recognition.money_recognition import execute_money_recognition
from scene_description.image_caption import execute_image_caption
from visual_question_answering.question_answering import execute_question_answering
from gps.gps import execute_send_gps

from blindverse.utils.consts import CAP_IMAGE_NAME
from blindverse.utils.capture_photo import take_capture
from blindverse.utils.micro_recog import record


from gpiozero import Button
from signal import pause
import translators as ts

selection_btn = Button(2)

confirm_btn = Button(3,hold_time=3,hold_repeat=False)

selected_mode = 0
is_gps_selected = 0
print(data_loaded)
string_to_speech(data_loaded,lang=get_lang())

def on_selection_pressed():
    global selected_mode
    selected_mode +=  1
    if selected_mode == 5:
        selected_mode = 1

    if selected_mode == 1:
        print(selected_mode_money)
        string_to_speech(selected_mode_money,lang=get_lang())
    if selected_mode == 2:
        print(selected_mode_product)
        string_to_speech(selected_mode_product ,lang=get_lang())
    if selected_mode == 3:
        print(selected_mode_scene)
        string_to_speech(selected_mode_scene,lang=get_lang())
    if selected_mode == 4:
        print(selected_mode_question)
        string_to_speech(selected_mode_question,lang=get_lang())

def on_confirm_pressed():
    global selected_mode, is_gps_selected
    result = "Please select a mode"
    if is_gps_selected == 1: 
        print("GPS ALERT")
        result = execute_send_gps()
        string_to_speech(result,lang=get_lang())

    if selected_mode == 1 and is_gps_selected == 0:
        print(confirmed_mode_money)
        string_to_speech(confirmed_mode_money,lang=get_lang()) 
        result = execute_money_recognition()
        print(result)
        string_to_speech(result,lang=get_lang())
    if selected_mode == 2 and is_gps_selected == 0:
        print(confirmed_mode_product)
        string_to_speech(confirmed_mode_product,lang=get_lang())
        result = execute_barcode_recognition()
        print(result)
        string_to_speech(result,lang=get_lang())
    if selected_mode == 3 and is_gps_selected == 0:
        print(confirmed_mode_scene)
        string_to_speech(confirmed_mode_scene,lang=get_lang())
        result = execute_image_caption(take_capture())
        if get_lang() != "en": 
            result_translated = ts.google(result, from_language='en', to_language=get_lang())
            print(result_translated)
            string_to_speech(result_translated,lang=get_lang())
        else:
            print(result)
            string_to_speech(result,lang=get_lang())
    if selected_mode == 4 and is_gps_selected == 0:
        print(confirmed_mode_question)
        string_to_speech(confirmed_mode_scene,lang=get_lang())
        question_to_answer = str(record())
        if get_lang() != "en":
            question_to_answer = ts.google(question_to_answer, from_language= get_lang(), to_language="en")
        print(your_question, ": ",question_to_answer)
        string_to_speech(your_question + question_to_answer,lang=get_lang())
        result = execute_question_answering(take_capture(),question_to_answer)
        if get_lang() != "en":
            print(result)
            result_translated = ts.google(result, from_language='en', to_language=get_lang())
            string_to_speech(result_translated,lang=get_lang())
        else:
            print(result)
            string_to_speech(result,lang=get_lang())

    is_gps_selected = 0

def on_held(): 
    global is_gps_selected
    is_gps_selected = 1

selection_btn.when_released = on_selection_pressed 
confirm_btn.when_released = on_confirm_pressed
confirm_btn.when_held = on_held

pause()
