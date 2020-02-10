import tensorflow as tf
import numpy as np
import cv2 as cv

def reversePic(src):
    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            src[i, j] = 255 - src[i, j]
    return src

sess = tf.Session()
saver = tf.train.import_meta_graph('model/MNIST.meta')
saver.restore(sess, 'model/MNIST')
x = sess.graph.get_tensor_by_name('x:0')
y = sess.graph.get_tensor_by_name('y:0')

def loadPic(path):
    raw_pic_0 = cv.imread(path, cv.IMREAD_GRAYSCALE)
    raw_pic_0 = reversePic(raw_pic_0)
    width = 28
    height = 28
    raw_pic = cv.resize(raw_pic_0, (width, height), interpolation=cv.INTER_CUBIC)
    cv.namedWindow('PIC_NN', cv.WINDOW_NORMAL)
    cv.imshow('PIC_NN', raw_pic)
    cv.waitKey(0)

    return raw_pic

while 1:
    raw_pic = loadPic('data/num.jpg')
    input_data = np.reshape(raw_pic, [-1, 784])
    result = sess.run(y, feed_dict={x: input_data})
    print('the predict is %d' % (np.argmax(result)))
    cv.waitKey(0)
