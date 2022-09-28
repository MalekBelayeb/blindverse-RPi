print("welcome to blindverse, loading data ...")
import time
import sys
sys.path.append('/home/pi/Desktop/blindverse-RPi/blindverse')

from barcode_recognition.barcode import execute_barcode_recognition
from money_recognition.money_recognition import execute_money_recognition
from scene_description.image_caption import execute_image_caption
from visual_question_answering.question_answering import execute_question_answering

from blindverse.utils.consts import CAP_IMAGE_NAME
from blindverse.utils.capture_photo import take_capture
from blindverse.utils.micro_recog import record

from gpiozero import Button
from signal import pause

selection_btn = Button(2)
confirm_btn = Button(3)
selected_mode = 0
print("Data loaded successfully, Please select your mode:")
def on_selection_pressed():
    global selected_mode
    selected_mode +=  1
    if selected_mode == 5:
        selected_mode = 1

    if selected_mode == 1:
        print("selected mode money recongnition")
    if selected_mode == 2:
        print("selected mode barcode")
    if selected_mode == 3:
        print("selected image caption")
    if selected_mode == 4:
        print("selected question answering")


def on_confirm_pressed():
    global selected_mode
    if selected_mode == 1:
        print("confirmed mode money recongnition")
        result = execute_money_recognition()
        print(result)
    if selected_mode == 2:
        print("confirmed mode barcode")
        result = execute_barcode_recognition()
        print(result)
    if selected_mode == 3:
        print("confirmed image caption")
        result = execute_image_caption(take_capture())
        print(result)
    if selected_mode == 4:
        print("confirmed question answering")
        question_to_answer = str(record())
        print("your question: ",question_to_answer)
        result = execute_question_answering(take_capture(),question_to_answer)
        print(result)


selection_btn.when_released = on_selection_pressed
confirm_btn.when_released = on_confirm_pressed

pause()
