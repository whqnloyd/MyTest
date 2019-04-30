import numpy as np
import cv2 as cv

img = cv.imread('test_pic.jpg')

img2 = np.array(img)

print(img2.shape)

img_gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)

while 1:
    cv.imshow('test', img_gray)
    cv.imshow('tets1', img_hsv)
    cv.imshow('o', img)
    if cv.waitKey(0) & 0xFF == ord('`'):
        break

cv.destroyAllWindows()


