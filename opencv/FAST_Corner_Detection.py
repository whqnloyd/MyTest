import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('image/dog.jpg', 0)

fast = cv2.FastFeatureDetector_create()

kp = fast.detect(image)
image = cv2.drawKeypoints(image, kp, image, color=(0, 0, 255))

cv2.imshow('pic', image)
cv2.waitKey(0)