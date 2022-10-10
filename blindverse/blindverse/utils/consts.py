import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
VIDEO_CAM_URL = 0
#VIDEO_CAM_URL = "http://10.54.234.71/cam-hi.jpg"
#BACKEND_URL = "http://192.168.43.124:80/imgcap/predict/v2/"
BACKEND_URL = "https://hf.space/embed/OFA-Sys/OFA-Image_Caption/api/predict/"
BACKEND_URL_vqa = "https://hf.space/embed/OFA-Sys/OFA-vqa/api/predict/"
#CAP_IMAGE_NAME = "{}/images/opencv_frame.png".format(PROJECT_ROOT)
CAP_IMAGE_NAME = "{}/opencv_frame.png".format(PROJECT_ROOT)
DURATION_OF_THE_QUESTION = 6 #6 seconds to ask the question
MONEY_DETECTION_MODEL = "{}/models/money-model.tflite".format(PROJECT_ROOT)
ADAFRUIT_IO_KEY = 'aio_tzaF313Fb7FXmbOTQDqVoedW0fHS'
ADAFRUIT_IO_USERNAME = 'blindverse'
SOCKET_SERVER_HOST = '192.168.1.151'
SOCKET_SERVER_PORT = 3000
