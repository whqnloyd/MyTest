import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("D:\MyTest\opencv\opencv-data\chessboard\chessboard.png", 0)          # queryImage
img1 = cv2.resize(img1, (0,0), fx=0.05, fy=0.05)
img2 = cv2.imread("D:\MyTest\opencv\opencv-data\chessboard\left04.jpg", 0)              # trainImage

# Initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# FLANN parameters
FLANN_INDEX_LSH = 6
index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 15,     # 20
                   multi_probe_level = 2) #2
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des1, des2, k=2)

img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None)

plt.imshow(img3)
plt.show()

# ORB
# # create BFMatcher object
# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# # Match descriptors.
# matches = bf.match(des1, des2)
# # Sort them in the order of their distance.
# matches = sorted(matches, key=lambda x: x.distance)
# # Draw first 10 matches.
# img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
#
# plt.imshow(img3)
# plt.show()
