import sys
sys.path.append('/home/blindverse/Desktop/blindverse-RPi/blindverse/')

import numpy as np
import tflite_runtime.interpreter as tflite
#import tensorflow as tf
import cv2
from PIL import Image
from blindverse.utils.consts import VIDEO_CAM_URL, MONEY_DETECTION_MODEL

def execute_money_recognition():

    cv2.namedWindow("test")
    img_counter = 0
    result = ""

    while True:
        cam = cv2.VideoCapture(VIDEO_CAM_URL)
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        # elif k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

        # Load TFLite model and allocate tensors.
        interpreter = tf.lite.Interpreter(model_path=MONEY_DETECTION_MODEL)
        interpreter.allocate_tensors()

        # Get input and output tensors.
        input_details = interpreter.get_input_details()

        # get input model shape.
        _, height, width, _ = input_details[0]['shape']

        image = Image.open("opencv_frame.png").resize((180, 180))

        # classify the image.
        input_tensor = np.array(np.expand_dims(image, 0), dtype=np.float32)

        input_index = interpreter.get_input_details()[0]["index"]

        interpreter.set_tensor(input_index, input_tensor)

        interpreter.invoke()

        output_details = interpreter.get_output_details()

        output_data = interpreter.get_tensor(output_details[0]['index'])

        prediction = np.squeeze(output_data)

        # prediction without score calculated
        class_names = {0: '10', 1: '20', 2: '5', 3: '50'}

        highest_pred_loc = np.argmax(prediction)

        result = "This image most likely belongs to {} dinars".format(class_names[highest_pred_loc])
        print("This image most likely belongs to {} dinars".format(class_names[highest_pred_loc]))

        break
    return result
