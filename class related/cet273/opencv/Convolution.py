import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('opencv_logo.png')
#Averaging
kernel = np.ones((5, 5), np.float32)/25
average_blur = cv.filter2D(img, -1, kernel)
#Gaussian Blurring
gaussian_blur = cv.GaussianBlur(img, (5, 5), 5)
#Median Blurring
median_blur = cv.medianBlur(img, 5)
#Bilateral Filtering
bilateral_blur = cv.bilateralFilter(img, 9, 75, 75)

plt.subplot(2, 3, 1), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 2), plt.imshow(average_blur), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 3), plt.imshow(gaussian_blur), plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 4), plt.imshow(median_blur), plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 5), plt.imshow(bilateral_blur), plt.title('Bilateral')
plt.xticks([]), plt.yticks([])

plt.show()