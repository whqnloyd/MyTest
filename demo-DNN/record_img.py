import cv2
import time

cap = cv2.VideoCapture(0)

i = 0
count = 0

while 1:
    i = i + 1

    ret, img = cap.read()
    cv2.imshow('cap', img)

    if i == 10:
        count = count + 1
        cv2.imwrite('saved/pic%d.jpg' % count, img)
        i = 0

    if cv2.waitKey(1) & 0xFF == ord('`'):
        break

cv2.destroyAllWindows()
