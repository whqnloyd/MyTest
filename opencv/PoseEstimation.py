import cv2
import numpy as np
import glob

criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((7*6, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)
# axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1, 3)
axis = np.float32([[0,0,0], [0,3,0], [3,3,0], [3,0,0],
                   [0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3] ])

obj_points = []
img_points = []

images = glob.glob('opencv-data/chessboard/*.jpg')

def draw(img, corners, imgpts):
    # corner = tuple(corners[0].ravel())
    # img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255, 0, 0), 5)
    # img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0, 255, 0), 5)
    # img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0, 0, 255), 5)
    # return img

    imgpts = np.int32(imgpts).reshape(-1, 2)

    # draw ground floor in green
    img = cv2.drawContours(img, [imgpts[:4]], -1, (0, 255, 0), -3)

    # draw pillars in blue color
    for i, j in zip(range(4), range(4, 8)):
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]), (255), 3)

    # draw top layer in red color
    img = cv2.drawContours(img, [imgpts[4:]], -1, (0, 0, 255), 3)

    return img

for frame in images:
    img = cv2.imread(frame)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners_ = cv2.findChessboardCorners(gray_img, (7, 6), None)
    if ret == True:
        obj_points.append(objp)
        corners2 = cv2.cornerSubPix(gray_img, corners_, (11, 11), (-1, -1), criteria)
        img_points.append(corners2)
        # cv2.drawChessboardCorners(img, (7, 6), corners2, ret)
        # cv2.imshow('img', img)
        # cv2.waitKey(0)

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points,
                                                   img_points,
                                                   gray_img.shape[::-1],
                                                   None,
                                                   None)

for frame in images:
    img = cv2.imread(frame)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray_img, (7, 6), None)
    if ret == True:
        corners2 = cv2.cornerSubPix(gray_img, corners, (11, 11), (-1, -1), criteria)
        _, rvecs, tvecs, liners = cv2.solvePnPRansac(objp, corners2, mtx, dist)
        # project 3D points to image plane
        imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)

        img = draw(img, corners2, imgpts)
        cv2.imshow('img', img)
        k = cv2.waitKey(0)
