import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image/stop_sign_base_1.jpg', 0)
img_1 = img.copy()
img_2 = img.copy()
img_3 = img.copy()
img_4 = img.copy()
template = cv2.imread('image/stop_sign_1.jpg', 0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
# first 2 are good for color change, and next 2 are good for distort
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
res = []
bottom_right_list = []
top_left_list = []
i = 0

for meth in methods:
    method = eval(meth)

    # Apply template Matching
    res.append(cv2.matchTemplate(img, template, method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res[i])

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    top_left_list.append(top_left)
    bottom_right = (top_left[0] + w, top_left[1] + h)
    bottom_right_list.append(bottom_right)
    print(top_left, bottom_right)

    i = i + 1

def draw_loc(img, i):
    cv2.rectangle(img, top_left_list[i], bottom_right_list[i], 255, 2)

def corp_target(img, x, y):
    print(x, y)
    crop_img = img[x[1]:y[1], x[0]:y[0]]
    # crop_img = img[y[1]:y[0], x[1]:x[0]]

    return crop_img

plt.figure(1)
plt.imshow(corp_target(img, top_left_list[0], bottom_right_list[0]), cmap='gray')
plt.xticks([])
plt.yticks([])
plt.figure(2)
plt.subplot(221)
draw_loc(img_1, 0)
plt.imshow(img_1, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.subplot(222)
draw_loc(img_2, 1)
plt.imshow(img_2, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.subplot(223)
draw_loc(img_3, 2)
plt.imshow(img_3, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.subplot(224)
draw_loc(img_4, 3)
plt.imshow(img_4, cmap='gray')
plt.xticks([])
plt.yticks([])

# plt.subplot(121), plt.imshow(res, cmap='gray')
# plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(img, cmap='gray')
# plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
# plt.suptitle(meth)
plt.show()
