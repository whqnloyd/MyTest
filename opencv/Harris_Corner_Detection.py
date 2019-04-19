import cv2
import numpy as np

path = 'image/dog.jpg'
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, gray_rev = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV)
kernel_fine = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
gray_rev = cv2.morphologyEx(gray_rev, cv2.MORPH_CLOSE, kernel_fine)

gray_rev = np.float32(gray_rev)
dst = cv2.cornerHarris(gray_rev, 3, 3, 0.04)
kernel_dilate = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dst = cv2.dilate(dst, kernel_dilate)
image[dst > 0.4 * dst.max()] = [0, 0, 255]
cv2.imshow('dst', image)

if cv2.waitKey(0) & 0xff == '`':
    cv2.destroyAllWindows()
