import cv2
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image/stop_sign_base_1.jpg', 0)
template = cv2.imread('image/stop_sign_2.jpg', 0)
w, h = template.shape[::-1]

# first 2 are good for color change, and next 2 are good for distort
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
methods = ['cv2.TM_CCOEFF_NORMED']
method = eval(methods[0])
res = cv2.matchTemplate(img, template, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
crop_img = img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
cv2.rectangle(img, top_left, bottom_right, 255, 2)
cv2.imshow('right?', img)
cv2.waitKey(0)

def reversePic(src):
    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            src[i, j] = 255 - src[i, j]
    return src

sess = tf.InteractiveSession()
saver = tf.train.import_meta_graph('model/CNN_MNIST.meta')
saver.restore(sess, 'model/CNN_MNIST')
input_x = sess.graph.get_tensor_by_name('x:0')
y = sess.graph.get_tensor_by_name('y:0')

def loadPic(im):
    # im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # im = reversePic(im)
    im = cv2.resize(im, (28, 28), interpolation=cv2.INTER_CUBIC)
    cv2.namedWindow('test', cv2.WINDOW_NORMAL)
    cv2.imshow('test', im)
    cv2.waitKey(0)

    return im

while 1:
    raw_pic = loadPic(crop_img)
    input_data = np.reshape(raw_pic, [-1, 784])
    output = sess.run(y, feed_dict={input_x: input_data})
    print('the predict is %d' % (np.argmax(output)))
    cv2.waitKey(0)

# plt.figure(1)
# plt.imshow(corp_target(img, top_left_list[0], bottom_right_list[0]), cmap='gray')
# plt.xticks([])
# plt.yticks([])
# plt.figure(2)
# plt.subplot(221)
# draw_loc(img_1, 0)
# plt.imshow(img_1, cmap='gray')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(222)
# draw_loc(img_2, 1)
# plt.imshow(img_2, cmap='gray')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(223)
# draw_loc(img_3, 2)
# plt.imshow(img_3, cmap='gray')
# plt.xticks([])
# plt.yticks([])
# plt.subplot(224)
# draw_loc(img_4, 3)
# plt.imshow(img_4, cmap='gray')
# plt.xticks([])
# plt.yticks([])

# plt.show()

