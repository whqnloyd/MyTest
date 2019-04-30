import cv2
import numpy as np
import glob

criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((7*6, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

obj_points = []
img_points = []

images = glob.glob('opencv-data/chessboard/*.jpg')

for frame in images:
    img = cv2.imread(frame)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray_img, (7, 6), None)
    if ret == True:
        obj_points.append(objp)
        corners2 = cv2.cornerSubPix(gray_img, corners, (11, 11), (-1, -1), criteria)
        img_points.append(corners)
#         cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
#         cv2.imshow('img', img)
#         cv2.waitKey(0)
# cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points,
                                                   img_points,
                                                   gray_img.shape[::-1],
                                                   None,
                                                   None)
sample_img = cv2.imread('opencv-data/chessboard/left02.jpg', 0)
h, w = sample_img.shape[:2]
new_matrix, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
dst = cv2.undistort(sample_img, mtx, dist, None, new_matrix)
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imshow('undistor', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()