import cv2
import numpy as np
from matplotlib import pyplot as plt

path = 'image/dog.jpg'
img_RGB = cv2.imread(path, 1)

mask = np.zeros(img_RGB.shape[:2], np.uint8)
width = img_RGB.shape[0]
length = img_RGB.shape[1]
mask[int(width/3):int(width/3*2), int(length/3):int(length/3*2)] = 255
masked_img = cv2.bitwise_and(img_RGB, img_RGB, mask=mask)

plt.figure(1)
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img_RGB, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(masked_img, cv2.COLOR_BGR2RGB))
plt.show()
