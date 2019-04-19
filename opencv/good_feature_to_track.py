import cv2
import numpy as np

path = 'image/dog.jpg'
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, gray_rev = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV)
kernel_fine = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
gray_rev = cv2.morphologyEx(gray_rev, cv2.MORPH_CLOSE, kernel_fine)
ret, gray = cv2.threshold(gray_rev, 0, 255, cv2.THRESH_BINARY_INV)

corners = cv2.goodFeaturesToTrack(gray, 10, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(image, (x,y), 3, 255, -1)

cv2.imshow('dst', image)

if cv2.waitKey(0) & 0xff == '`':
    cv2.destroyAllWindows()
