import cv2
from time import sleep
import numpy as np
def Hue_min(a):
    # print("Hue_min value: " + str(a))
    pass
def Hue_max(a):
    # print("Hue_max value: " + str(a))
    pass
def Sat_min(a):
    # print("Sat_min value: " + str(a))
    pass
def Sat_max(a):
    # print("Sat_max value: " + str(a))
    pass
def Val_min(a):
    # print("Val_min value: " + str(a))
    pass
def Val_max(a):
    # print("Val_max value: " + str(a))
    pass

# ****************************************************
def Hue_min_val():
    # print("Hue_min value: " + str(a))
    a = cv2.getTrackbarPos("Hue Min", "TrackBars")
    return a
def Hue_max_val():
    # print("Hue_max value: " + str(a))
    a = cv2.getTrackbarPos("Hue Max", "TrackBars")
    return a
def Sat_min_val():
    # print("Sat_min value: " + str(a))
    a = cv2.getTrackbarPos("Sat Min", "TrackBars")
    return a
def Sat_max_val():
    # print("Sat_max value: " + str(a))
    a = cv2.getTrackbarPos("Sat Max", "TrackBars")
    return a
def Val_min_val():
    # print("Val_min value: " + str(a))
    a = cv2.getTrackbarPos("Val Min", "TrackBars")
    return a
def Val_max_val():
    # print("Val_max value: " + str(a))
    a = cv2.getTrackbarPos("Val Max", "TrackBars")
    return a
def Cascade_1():
    # print("Val_max value: " + str(a))
    a = cv2.getTrackbarPos("Cascade 1", "TrackBars")
    return a
def Cascade_2():
    # print("Val_max value: " + str(a))
    a = cv2.getTrackbarPos("Cascade 2", "TrackBars")
    return a

def proto():
    img = cv2.imread("lenna.png")
    cv2.imshow("Image", img)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", imgHSV)
    h_min = Hue_min_val()
    s_min = Sat_min_val()
    v_min = Val_min_val()
    h_max = Hue_max_val()
    s_max = Sat_max_val()
    v_max = Val_max_val()
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    imgrn = cv2.inRange(imgHSV, lower, upper)

    cv2.imshow("MASK", imgrn)



cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 480)
cv2.createTrackbar("Hue Min", "TrackBars",110 ,1366, Hue_min)
cv2.createTrackbar("Hue Max", "TrackBars",179 ,179, Hue_max)
cv2.createTrackbar("Sat Min", "TrackBars",50 ,255, Sat_min)
cv2.createTrackbar("Sat Max", "TrackBars",255 ,255, Sat_max)
cv2.createTrackbar("Val Min", "TrackBars",50 ,255, Val_min)
cv2.createTrackbar("Val Max", "TrackBars",255 ,255, Val_max)
cv2.createTrackbar("Cascade 1", "TrackBars",1 ,5, Val_max)
cv2.createTrackbar("Cascade 2", "TrackBars",4 ,5, Val_max)



if __name__ == "__main__":
    while True:
        # proto()
        img1 = cv2.imread("lenna.png")
        img = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h_min = Hue_min_val()
        s_min = Sat_min_val()
        v_min = Val_min_val()
        h_max = Hue_max_val()
        s_max = Sat_max_val()
        v_max = Val_max_val()
        # upper = np.array(h_max, s_max, v_max)
        # lower = np.array(h_min, s_min, v_min)
        # print(lower, upper)
        imgrn = cv2.inRange(imgHSV, (h_min, s_min, v_min), (h_max, s_max, v_max))
        cv2.imshow("Image", img)
        cv2.imshow("HSV", imgHSV)
        cv2.imshow("MASK", imgrn)

        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
