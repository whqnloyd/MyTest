import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)

path = 'image/dog.jpg'
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, gray_rev = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV)
kernel_fine = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
gray_rev = cv2.morphologyEx(gray_rev, cv2.MORPH_CLOSE, kernel_fine)
ret, gray = cv2.threshold(gray_rev, 0, 255, cv2.THRESH_BINARY_INV)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 3, 3, 0.04)
kernel_dilate = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dst = cv2.dilate(dst, kernel_dilate)
ret, dst = cv2.threshold(dst, 0.4*dst.max(), 255, 0)
# image[dst > 0.4 * dst.max()] = [0, 0, 255]

dst = np.uint8(dst)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)

# print(centroids)
# print(corners)
res = np.hstack((centroids, corners))
res = np.int0(res)
image[res[:, 1], res[:, 0]] = [0, 0, 255]
image[res[:, 3], res[:, 2]] = [0, 255, 0]
cv2.imshow('dst', image)

if cv2.waitKey(0) & 0xff == '`':
    cv2.destroyAllWindows()
