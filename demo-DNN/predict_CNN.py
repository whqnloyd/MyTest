import cv2
import tensorflow as tf
import numpy as np

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

def loadPic(path):
    im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    im = reversePic(im)
    im = cv2.resize(im, (28, 28), interpolation=cv2.INTER_CUBIC)
    cv2.namedWindow('pic_CNN', cv2.WINDOW_NORMAL)
    cv2.imshow('pic_CNN', im)
    cv2.waitKey(0)

    return im

while 1:
    raw_pic = loadPic('data/num.jpg')
    input_data = np.reshape(raw_pic, [-1, 784])
    output = sess.run(y, feed_dict={input_x: input_data})
    print('the predict is %d' % (np.argmax(output)))
    cv2.waitKey(0)
