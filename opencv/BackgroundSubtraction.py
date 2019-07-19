import numpy as np
import cv2

cap = cv2.VideoCapture('opencv-data/vtest.avi')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.createBackgroundSubtractorMOG2()

while 1:
    ret, frame = cap.read()

    fgmask = cv2.morphologyEx(fgbg.apply(frame), cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()