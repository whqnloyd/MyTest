import cv2
import numpy as np
from matplotlib import pyplot as plt

path = 'image/dog.jpg'
img_RGB = cv2.imread(path, 1)
img_gray = cv2.imread(path, 0)

hist_gray = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
RGB_list = ['red', 'green', 'blue']
hist_RGB = []
for i in range(3):
    hist_RGB.append(cv2.calcHist([img_RGB], [i], None, [256], [0, 256]))

for i in range(3):
    plt.figure(1)
    plt.subplot(1, 3, i+1)
    plt.bar(range(len(hist_RGB[i])), hist_RGB[i].ravel(), color=RGB_list[i])

plt.figure(2)
plt.bar(range(len(hist_gray)), hist_gray.reshape(1, -1)[0])

plt.figure(3)
plt.hist(img_gray.ravel(), 256, [0, 256])

plt.figure(4)
plt.hist(img_RGB.ravel(), 256, [0, 256])

plt.show()