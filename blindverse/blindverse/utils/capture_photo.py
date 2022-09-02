import cv2
from consts import VIDEO_CAM_URL

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
    return img_name
