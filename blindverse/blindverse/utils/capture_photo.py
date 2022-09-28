import cv2
import sys

sys.path.append('/home/pi/Desktop/blindverse-RPi/blindverse')

from blindverse.utils.consts import VIDEO_CAM_URL
from blindverse.utils.consts import PROJECT_ROOT
def capture_image():
    cv2.namedWindow("test")
    img_counter = 0
    while True:
        cam = cv2.VideoCapture(VIDEO_CAM_URL)
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "opencv_frame.png"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
    return "{}/"+img_name.format(PROJECT_ROOT)


def take_capture():

    cam = cv2.VideoCapture(VIDEO_CAM_URL)
    ret, frame = cam.read()
    img_name = "opencv_frame.png"
    image_path = ("{}/images/"+img_name).format(PROJECT_ROOT)
    cv2.imwrite(image_path, frame)
    cam.release()
    return image_path
    