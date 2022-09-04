import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
VIDEO_CAM_URL = 0
#VIDEO_CAM_URL = "http://192.168.43.87/cam-hi.jpg"
#BACKEND_URL = "http://192.168.43.124:80/imgcap/predict/v2/"
BACKEND_URL = "https://hf.space/embed/OFA-Sys/OFA-Image_Caption/api/predict/"
CAP_IMAGE_NAME = "{}/images/opencv_frame.png".format(PROJECT_ROOT)
MONEY_DETECTION_MODEL = "{}/models/money-model.tflite".format(PROJECT_ROOT)
ADAFRUIT_IO_KEY = 'aio_tzaF313Fb7FXmbOTQDqVoedW0fHS'
ADAFRUIT_IO_USERNAME = 'blindverse'