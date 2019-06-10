import cv2
import numpy as np

path = 'opencv-data/chessboard/left01.jpg'
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
kp = sift.detect(gray, None)

