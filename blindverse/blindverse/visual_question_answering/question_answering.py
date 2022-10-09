import sys
sys.path.append('/home/pi/Desktop/blindverse-RPi/blindverse')
import requests
import os
import json
import base64
from blindverse.utils.consts import BACKEND_URL_vqa

def execute_question_answering(path_img, text):
    with open(path_img, 'rb') as img:
        name_img = os.path.basename(path_img)
        encoded_string = base64.b64encode(img.read())
        body_request = {"data": ["data:image/jpeg;base64,{}".format(encoded_string.decode('utf-8')), text],
                         "session_hash": "njsvyejq5hc"}

        with requests.Session() as s:
            res = s.post(BACKEND_URL_vqa, json.dumps(body_request))
            
            return json.loads(res.text)['data'][0]

    return ""

