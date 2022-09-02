import cv2
from pyzbar.pyzbar import decode
import requests
import json
from blindverse.utils.consts import VIDEO_CAM_URL

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

    while True:

        cap = cv2.VideoCapture(VIDEO_CAM_URL)  # 'http://192.168.43.87/cam-hi.jpg'
        # cap.set(3, 640)
        # cap.set(4, 480)
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

    r = requests.get('https://tn.openfoodfacts.org/api/v2/search?code=' + str(myData) + '&fields=product_name')
    product_name = json.loads(r.content.decode('utf-8'))['products'][0]['product_name']
    print(product_name)
    return product_name

