import cv2
import tensorflow as tf
import numpy as np

def reversePic(src):
    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            src[i, j] = 255 - src[i, j]
    return src

sess = tf.InteractiveSession()
saver = tf.train.import_meta_graph('model/car_model.meta')
saver.restore(sess, 'model/car_model')
input_x = sess.graph.get_tensor_by_name('x:0')
y = sess.graph.get_tensor_by_name('y:0')

def loadPic(path):
    im = cv2.imread(path, 0)
    # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # im = reversePic(im)
    im = cv2.resize(im, (32, 32), interpolation=cv2.INTER_CUBIC)
    cv2.namedWindow('pic_CNN', cv2.WINDOW_NORMAL)
    cv2.imshow('pic_CNN', im)
    # cv2.waitKey(0)

    return im

count = 0
while 1:
    count = count + 5
    raw_pic = loadPic('images/pic%d.jpg' % count)
    input_data = np.reshape(raw_pic, [1, 1024])
    output = sess.run(y, feed_dict={input_x: input_data})
    print(output)
    key = np.argmax(output)
    if key == 0:
        print('left')
    elif key == 1:
        print('go straight')
    elif key == 2:
        print('right')
    cv2.waitKey(0)
