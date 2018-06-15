import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret1, img = cap.read()
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low_range = np.array([0, 0, 0])
    hign_range = np.array([180, 255, 46])
    img3 = cv2.inRange(img2, low_range, hign_range)
    ret2, img4 = cv2.threshold(img3, 127, 255, cv2.THRESH_BINARY_INV)       #黑白反转
    mask1 = cv2.erode(img3, None, iterations=2)
    mask2 = cv2.dilate(mask1, None, iterations=7)
#    mask3 = cv2.erode(mask2, None, iterations=7)
    img5, cnts, hierarchy = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, cnts, -1, (0, 0, 360), 1)
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if 100000 > area > 60000:
            rect = cv2.minAreaRect(cnt)
            x, y = rect[0]
            width, length = rect[1]
#            length = rect[1][1]
            angle = rect[2]
            print('x:%.2f y:%.2f width:%.2f length:%.2f angle:%.2f' % (x, y, width, length, angle))
            cv2.circle(img, (int(x), int(y)), 3, (360, 0, 0), 2)

#   are=cv2.
#   if circles is not None:
#        x,y,radius=circles[0][0]
#        center=(x,y)
#        cv2.circle(img,center,radius,(0,255,0),2)

    cv2.imshow('result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()