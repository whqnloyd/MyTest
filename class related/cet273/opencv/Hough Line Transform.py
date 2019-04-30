import cv2 as cv
import numpy as np

img = cv.imread('road_lines.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 100, 200, apertureSize=3)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=200, maxLineGap=1)

while 1:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv.imshow('houghlines3.jpg', img)
    cv.imshow('lines', edges)
    if cv.waitKey(0) & 0xFF == ord('`'):
        break
cv.destroyAllWindows()

