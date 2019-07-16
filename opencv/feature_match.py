import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("D:\\MyTest\\opencv\\opencv-data\\box.png", 0)          # queryImage
# img1 = cv2.resize(img1, (0,0), fx=0.05, fy=0.05)
img2 = cv2.imread("D:\\MyTest\\opencv\\opencv-data\\box_in_scene.png", 0)              # trainImage

# Initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# FLANN parameters
FLANN_INDEX_LSH = 6
index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 12, # 12
                   key_size = 20,     # 20
                   multi_probe_level = 2) #2
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des1, des2, k=2)

good = []
for i in matches:
    if len(i) == 2:
        m = i[0]
        n = i[1]
        if m.distance < 0.7*n.distance:
            good.append(m)
    else:
        continue

if len(good)>10:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()

    h,w = img1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)

    img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

else:
    print("Not enough matches are found - %d/%d" % (len(good), 10))
    matchesMask = None

draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)

plt.imshow(img3, 'gray')
plt.show()

# img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None)
#
# plt.imshow(img3)
# plt.show()

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
