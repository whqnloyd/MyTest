import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#img = cv2.

while (1):
    ret1, img = cap.read()
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low_range = np.array([0,0,0])
    hign_range = np.array([360,120,120])
    img3 = cv2.inRange(img2, low_range, hign_range)
    ret2,img4 = cv2.threshold(img3, 127, 255, cv2.THRESH_BINARY_INV)
    img5, cnts, hierarchy = cv2.findContours(img4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img5,cnts,-1,(120,120,0),2)
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if area > 200:
            rect = cv2.minAreaRect(cnt)
            x,y= rect[0]
            cv2.circle(img5,(int(x),int(y)),2,(120,120,0),3)
#are=cv2.
#    if circles is not None:
#        x,y,radius=circles[0][0]
#        center=(x,y)
#        cv2.circle(img,center,radius,(0,255,0),2)
    cv2.imshow('result', img5)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()