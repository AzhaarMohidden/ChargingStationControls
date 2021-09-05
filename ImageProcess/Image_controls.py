import os
import numpy as np
import time
import cv2
import image_controller as ic

import pytesseract

cwd = os.getcwd()
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# x=364
# y=92
# w=70
# h=210

# x=364
# y=103
# w=70
# h=16

def track_values():
    # h_min = int(ic.Hue_min_val())
    x = int(ic.Hue_min_val())
    # s_min = int(ic.Sat_min_val())
    y = int(ic.Sat_min_val())
    # v_min = int(ic.Val_min_val())
    h = int(ic.Val_min_val())
    # h_max = int(ic.Hue_max_val())
    w = int(ic.Hue_max_val())
    s_max = int(ic.Sat_max_val())
    v_max = int(ic.Val_max_val())
    # return np.array([h_min,s_min,v_min]), np.array([h_max,s_max,v_max])
    # return np.array([h_min,s_min,v_min]), np.array([h_max,s_max,v_max])
    return x, y, h, w



def print_cwd():
    print(cwd)


def openImg():
    while(1):
        x, y, h, w= track_values()
        img = cv2.imread("test.png",cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # gryblr = cv2.GaussianBlur(gry,(lower[0],lower[1]),lower[2])
        # img = cv2.Canny(img,upper[0],upper[1])
        cropped = img[y:y + h, x:x + w]
        imgresize = cv2.resize(cropped,(360, 200))
        cv2.rectangle(img,(x,y),(x+w, y + h), (0,0,255),1)

        text = str(pytesseract.image_to_string(imgresize))

        print(text)

        # height, width = img.shape[:2]
        # print(width,' ' , height)
        cv2.imshow("IMAGE", img)
        cv2.imshow('cc',imgresize)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            # threading.Thread(target=frame_rate).join()
            # is_alive = 0
            break
    # cv2.waitKey(0)
    # time.sleep(2)


if __name__ == '__main__':
    openImg()
