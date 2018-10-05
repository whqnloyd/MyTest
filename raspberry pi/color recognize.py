import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = 640
height = 480
angle = 180
fps = 29

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, fps)


def rotate(img, ang, center=None, scale=None): 
    (h, w) = img.shape[:2] 
    if center == None:
        center = (w // 2, h // 2)
    if scale == None:
        scale = 1.0

    M = cv2.getRotationMatrix2D(center, ang, scale) 

    rot = cv2.warpAffine(img, M, (w, h)) 
    return rot

while True:
    ret1, frame = cap.read()
    image1 = rotate(frame, angle)
    image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
    low_range = np.array([0, 0, 0])
    hign_range = np.array([180, 255, 46])
    image3 = cv2.inRange(image2, low_range, hign_range)
    ret2, image4 = cv2.threshold(image3, 127, 255, cv2.THRESH_BINARY_INV)       #黑白反转
    mask1 = cv2.erode(image3, None, iterations=2)
    mask2 = cv2.dilate(mask1, None, iterations=7)
#    mask3 = cv2.erode(mask2, None, iterations=7)
    image5, cnts, hierarchy = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if 30000 > area > 10000:
            cv2.drawContours(image1, cnt, -1, (0, 0, 360), 1)
            rect = cv2.minAreaRect(cnt)
            x, y = rect[0]
            width, length = rect[1]
#            length = rect[1][1]
            ang = rect[2]
            print('x:%.2f y:%.2f width:%.2f length:%.2f angle:%.2f' % (x, y, width, length, ang))
            cv2.circle(image1, (int(x), int(y)), 3, (360, 0, 0), 2)

#   are=cv2.
#   if circles is not None:
#        x,y,radius=circles[0][0]
#        center=(x,y)
#        cv2.circle(img,center,radius,(0,255,0),2)

    cv2.imshow('result', image1)
    if cv2.waitKey(1) & 0xFF == ord('`'):
        break
cap.release()
cv2.destroyAllWindows()