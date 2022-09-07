import sys
sys.path.append('/home/blindverse/Desktop/blindverse-RPi/blindverse/')

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
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture(VIDEO_CAM_URL)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:

        #cap = cv2.VideoCapture(VIDEO_CAM_URL)  # 'http://192.168.43.87/cam-hi.jpg'
        

        success, img = cap.read()
        myData = decod_bar(img)
        print(myData)

        if not myData:
            cv2.imshow('Result', img)
        else:
            break

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
    cap.release()
    cv2.destroyAllWindows()
    '''
     

    url = VIDEO_CAM_URL
    stream=urlopen(r'http://10.54.234.71/cam-hi.jpg')
    stream_bytes = ''

    while True:
           
            stream_bytes += stream.read(1024)
            first = stream_bytes.find(b'\xff\xd8')
            last = stream_bytes.find(b'\xff\xd9')
            if first != -1 and last != -1:
                jpg = stream_bytes[first:last + 2]
                stream_bytes = stream_bytes[last + 2:]
                image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                myData = decod_bar(image)
                print(myData)
                cv2.imshow('image', image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
       # this  is required to deal with error due to blank frames received 
    print("here")
        '''
        

    r = requests.get('https://tn.openfoodfacts.org/api/v2/search?code=' + str(myData) + '&fields=product_name')
    product_name = json.loads(r.content.decode('utf-8'))['products'][0]['product_name']
    print(product_name)
    return product_name



