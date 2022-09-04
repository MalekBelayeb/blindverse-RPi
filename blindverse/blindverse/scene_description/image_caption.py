import sys
sys.path.append('/home/blindverse/Desktop/blindverse-RPi/blindverse/')
import requests
import os
import json
import base64
from blindverse.utils.consts import BACKEND_URL


def execute_image_caption(path_img):
    with open(path_img, 'rb') as img:
        name_img = os.path.basename(path_img)
        encoded_string = base64.b64encode(img.read())
        body_request = {"data": ["data:image/jpeg;base64,{}".format(encoded_string.decode('utf-8'))],
                         "session_hash": "0wdrus73qd3"}

        with requests.Session() as s:
            res = s.post(BACKEND_URL, json.dumps(body_request))
            print(json.loads(res.text)['data'][0])
            return  ""

    return ""

