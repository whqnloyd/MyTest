import cv2
import numpy as np
from matplotlib import pyplot as plt

#roi is the object or region of object we need to find
roi = cv2.imread('image/stop_sign_3.jpg')
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

#target is the image we search in
target = cv2.imread('image/stop_sign_base_1.jpg')
target = cv2.resize(target, (0, 0), fx=0.5, fy=0.5)
hsv_target = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

# Find the histograms using calcHist. Can be done with np.histogram2d also
roihist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
# cv2.imshow('1', roihist)
# cv2.waitKey(0)
# targethist = cv2.calcHist([hsv_target], [0, 1], None, [180, 256], [0, 180, 0, 256])
# cv2.imshow('2', targethist)
# cv2.waitKey(0)
# cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsv_target], [0, 1], roihist, [0, 180, 0, 256], 1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
cv2.filter2D(dst, -1, disc, dst)

# threshold and binary AND
ret, thresh = cv2.threshold(dst, 100, 255, cv2.THRESH_BINARY)
thresh = cv2.merge((thresh, thresh, thresh))   # RGB 3D
res = cv2.bitwise_and(target, thresh)
res = np.vstack((target, thresh, res))

cv2.imshow('res', res)
cv2.waitKey(0)
