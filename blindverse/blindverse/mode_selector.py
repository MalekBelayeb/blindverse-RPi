from blindverse.utils.audio_config import string_to_speech
string_to_speech("welcome to blindverse, loading data ...",lang='en')
print("welcome to blindverse, loading data ...")
import time
import sys


sys.path.append('/home/pi/Desktop/blindverse-RPi/blindverse')
from barcode_recognition.barcode import execute_barcode_recognition
from money_recognition.money_recognition import execute_money_recognition
from scene_description.image_caption import execute_image_caption
from visual_question_answering.question_answering import execute_question_answering
from gps.gps import execute_send_gps

from blindverse.utils.consts import CAP_IMAGE_NAME
from blindverse.utils.capture_photo import take_capture
from blindverse.utils.micro_recog import record
from blindverse.utils.audio_config import string_to_speech

from gpiozero import Button
from signal import pause
import translators as ts

selection_btn = Button(2)

confirm_btn = Button(3,hold_time=3,hold_repeat=False)

selected_mode = 0
is_gps_selected = 0
print("Data loaded successfully, Please select your mode:")
string_to_speech("Data loaded successfully, Please select your mode:",lang="en")

def on_selection_pressed():
    global selected_mode
    selected_mode +=  1
    if selected_mode == 5:
        selected_mode = 1

    if selected_mode == 1:
        print("selected mode money recongnition")
        string_to_speech("selected mode money recongnition",lang="en")
    if selected_mode == 2:
        print("selected mode barcode")
        string_to_speech("selected mode barcode",lang="en")
    if selected_mode == 3:
        print("selected image caption")
        string_to_speech("selected image caption",lang="en")
    if selected_mode == 4:
        print("selected question answering")
        string_to_speech("selected question answering",lang="en")

def on_confirm_pressed():
    global selected_mode, is_gps_selected
    result = "Please select a mode"
    if is_gps_selected == 1: 
        print("GPS ALERT")
        result = execute_send_gps()

    if selected_mode == 1 and is_gps_selected == 0:
        print("confirmed mode money recongnition")
        string_to_speech("confirmed mode money recongnition",lang="en") 
        result = execute_money_recognition()
        print(result)
        string_to_speech(result,lang="en")
    if selected_mode == 2 and is_gps_selected == 0:
        print("confirmed mode barcode")
        string_to_speech("confirmed mode barcode",lang="en")
        result = execute_barcode_recognition()
        print(result)
        string_to_speech(result,lang="en")
    if selected_mode == 3 and is_gps_selected == 0:
        print("confirmed image caption")
        string_to_speech("confirmed mode scene description",lang="en")
        result = execute_image_caption(take_capture())
        print(result)
        result_translated = ts.google(result, from_language='en', to_language='fr')
        #print(result_translated)
        string_to_speech(result_translated,lang="fr")

    if selected_mode == 4 and is_gps_selected == 0:
        print("confirmed question answering")
        string_to_speech("confirmed question answering",lang="en")
        question_to_answer = str(record())
        print("your question: ",question_to_answer)
        string_to_speech("your question: "+question_to_answer,lang="en")
        result = execute_question_answering(take_capture(),question_to_answer)
        print(result)
        string_to_speech(result,lang="en")

    
    
    is_gps_selected = 0

def on_held(): 
    global is_gps_selected
    is_gps_selected = 1

selection_btn.when_released = on_selection_pressed 
confirm_btn.when_released = on_confirm_pressed
confirm_btn.when_held = on_held

pause()
