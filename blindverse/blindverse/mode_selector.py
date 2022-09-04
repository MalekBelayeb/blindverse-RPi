import time
import sys
sys.path.append('/home/blindverse/Desktop/blindverse-RPi/blindverse/')

from barcode_recognition.barcode import execute_barcode_recognition
from money_recognition.money_recognition import execute_money_recognition
from scene_description.image_caption import execute_image_caption
from blindverse.utils.consts import CAP_IMAGE_NAME

"""
+++++++++++++++++++++++++ GPS ALERT +++++++++++++++++++++++++
content = 'AAAA' ====> GPS ALERT

+++++++++++++++++++++++++ MODE MONEY RECOGNITION +++++++++++++++++++++++++
content = '0000'
valdmod = 2
selectedmode = '1111'

+++++++++++++++++++++++++ MODE SCENE DESCRIPTION +++++++++++++++++++++++++
content = '1111'
valdmod = 2
selectedmode = '2222'

+++++++++++++++++++++++++ MODE BARCODE +++++++++++++++++++++++++
content = '2222'
valdmod = 2
selectedmode = '3333'

"""


def mode_selector(s):
    content = 0
    valdmod = 0
    selectedmode = '0'
    inmode = 0
    
    #FAKE VALUES
    content = '0000'
    valdmod = 2
    selectedmode = '1111'
    
    while True:
        #client, addr = s.accept()
        while True:
            #content = client.recv(32)
            
            if len(content) == 0:
                break
            else:
                # print(len(str(content))) # = 4
                if len(str(content)) == 4:

                    inmode = str(content)
                    # len(inmode) = 4
                    print(str(inmode[2]))
                    
                    if (str(inmode[2]) == '0'):
                        print('mode 0')

                    if (str(inmode[2]) == '1'):
                        print('mode 1')

                    if (str(inmode[2]) == '2'):
                        print('mode 2')

                    if (str(inmode[2]) == '3'):
                        print('mode 3')

                if len(str(content)) == 5:
                    selectedmode = str(inmode)
                    print("selectedmode is :  ", str(selectedmode))
                    valdmod += 1

                if valdmod == 2:

                    if (selectedmode[2] == '1'):
                        print('Mode Money is running')
                        valdmod = 0
                    
                        return execute_money_recognition()
                        
                    if (selectedmode[2] == '2'):
                        print('Mode scene description is running')
                        valdmod = 0
                        content = 0
            
                        return execute_image_caption(CAP_IMAGE_NAME)
                        
                    if (selectedmode[2] == '3'):
                        print('Mode barcode is running')
                        valdmod = 0
                        return execute_barcode_recognition()
                        
                    
                if (str(content)[2] == 'A'):
                    print("ALEEEEEEEET gps position sent")

                    valdmod = 0

                    for i in range(4):
                        execute_send_gps()
                        print("Iteration", i)
                        time.sleep(0.5)

        print("Closing connection")
        #client.close()

