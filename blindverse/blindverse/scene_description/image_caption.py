import requests
import os
import json
from blindverse.utils.consts import BACKEND_URL

def execute_image_caption(path_img):
    with open(path_img, 'rb') as img:
        name_img = os.path.basename(path_img)
        files = {'image': (name_img, img, 'multipart/form-data', {'Expires': '0'})}
        with requests.Session() as s:
            res = s.post(BACKEND_URL, files=files)
            print(res.text)
            return json.loads(res.text)['data']
    return ""

