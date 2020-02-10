import tensorflow as tf
import numpy as np
import cv2 as cv

# function for reverse your image, the input should be the image matrix
def reversePic(src):
    # reverse image
    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            src[i, j] = 255 - src[i, j]
    return src

# your image file path
path_pic = 'data/num2.jpg'

# load your image file as gray color format
raw_pic_0 = cv.imread(path_pic, cv.IMREAD_GRAYSCALE)

# reverse your image
raw_pic_0 = reversePic(raw_pic_0)

# setup(resize) the width and height (fit your model)
width = 28
height = 28
raw_pic = cv.resize(raw_pic_0, (width, height), interpolation=cv.INTER_CUBIC)

# show the image after reverse and resize (visible result for verification)
cv.namedWindow('PIC', cv.WINDOW_NORMAL)
cv.imshow('PIC', raw_pic)
cv.waitKey(0)

# start your the function for NN to run and load your model
sess = tf.Session()

saver = tf.train.import_meta_graph('model/MNIST.meta')
saver.restore(sess, 'model/MNIST')

# change your image matrix into flatten format [28,28] to [1,784] to fit your NN
input_data = np.reshape(raw_pic, [-1, 784])

# load the format for input data and output data
x = sess.graph.get_tensor_by_name('x:0')
y = sess.graph.get_tensor_by_name('y:0')

#
result = sess.run(y, feed_dict={x: input_data})
print('the predict is %d' % (np.argmax(result)))
