import cv2

path = 'image/dog.jpg'
img_gray = cv2.imread(path, 0)

equ = cv2.equalizeHist(img_gray)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(64, 64))
cl1 = clahe.apply(img_gray)

cv2.imshow('ori', img_gray)
cv2.imshow('equ', equ)
cv2.imshow('cll', cl1)
cv2.waitKey(0)
