import sys
sys.path.append('/home/pi/Desktop/blindverse-RPi/blindverse')

import cv2
from pyzbar.pyzbar import decode
import requests
import json

from blindverse.utils.consts import VIDEO_CAM_URL
from urllib.request import urlopen
import numpy as np


def decod_bar(img):
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        # pts = np.array([barcode.polygon], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        # pts2 = barcode.rect
        # cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
        if not myData:
            continue
        else:
            return myData

def execute_barcode_recognition():
    cap = cv2.VideoCapture(VIDEO_CAM_URL)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        success, img = cap.read()
        myData = decod_bar(img)
        print(myData)
        if myData:
            break

    cap.release()
    r = requests.get('https://tn.openfoodfacts.org/api/v2/search?code=' + str(myData) + '&fields=product_name')
    try:
        product_name = json.loads(r.content.decode('utf-8'))['products'][0]['product_name']
        return product_name
    except:
        return 'Product not found'

