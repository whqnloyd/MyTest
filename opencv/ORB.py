import numpy as np
import cv2
from matplotlib import pyplot as plt

path = 'D:\MyTest\opencv\image\stop_sign_4.jpg'
img = cv2.imread(path, 0)

# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
# compute the descriptors with ORB
kp, des = orb.detectAndCompute(img, None)
print(des.shape)
print(des)

# draw only keypoints location,not size and orientation
img = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
plt.imshow(img)
plt.show()
