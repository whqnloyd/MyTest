import tensorflow as tf
import numpy as np
import pandas as pd

train_data_path = 'images.csv'
train_size = 3

x = tf.placeholder(tf.float32, [None, 1024], name='x')   # training data, total res
x_reshape = tf.reshape(x, [-1, 32, 32, 1])              # training images, change to aspect size of image
labels = tf.placeholder(tf.float32, [None, 3])

def weight_variable(shape):
    initial = tf.truncated_normal(shape=shape, stddev=0.01)
    # initial = tf.zeros(shape)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.truncated_normal(shape=shape, stddev=0.1)
    # initial = tf.zeros(shape)
    return tf.Variable(initial)

def convolution(c_x, c_w):
    return tf.nn.conv2d(c_x, c_w, strides=[1, 1, 1, 1], padding='SAME')

def max_pool(p_x):
    return tf.nn.max_pool(p_x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

layer1 = 16
layer2 = 32
# layer3 = 64
# layer4 = 128
# layer5 = 128

dc_layer = 64
out_layer = 3

w_conv1 = weight_variable([32, 32, 1, layer1])
b_conv1 = bias_variable([layer1])
w_conv2 = weight_variable([8, 8, layer1, layer2])
b_conv2 = bias_variable([layer2])
# w_conv3 = weight_variable([4, 4, layer2, layer3])
# b_conv3 = bias_variable([layer3])
# w_conv4 = weight_variable([5, 5, layer3, layer4])
# b_conv4 = bias_variable([layer4])
# w_conv5 = weight_variable([5, 5, layer4, layer5])
# b_conv5 = bias_variable([layer5])

conv1 = tf.nn.relu(convolution(x_reshape, w_conv1) + b_conv1)
conv2 = tf.nn.relu(convolution(conv1, w_conv2) + b_conv2)
pool1 = max_pool(conv2)
# conv3 = tf.nn.relu(convolution(conv2, w_conv3) + b_conv3)

# conv3 = tf.nn.relu(convolution(pool1, w_conv3) + b_conv3)
# conv4 = tf.nn.relu(convolution(conv3, w_conv4) + b_conv4)
# conv5 = tf.nn.relu(convolution(conv4, w_conv5) + b_conv5)
# pool2 = max_pool(conv5)

w_dc = weight_variable([16 * 16 * layer2, dc_layer])
b_dc = bias_variable([dc_layer])

pool_flat = tf.reshape(pool1, [-1, 16 * 16 * layer2])
h_fc1 = tf.nn.relu(tf.matmul(pool_flat, w_dc) + b_dc, name='y_')

w_out = weight_variable([dc_layer, out_layer])
b_out = bias_variable([out_layer])

# y = tf.nn.softmax(tf.matmul(h_fc1_drop, w_out) + b_out, name='y_drop')
y = tf.nn.softmax(tf.matmul(h_fc1, w_out) + b_out, name='y')

loss = -tf.reduce_sum(labels*tf.log(y))
# loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=y, labels=labels))        # sum和mean的区别

# train_step = tf.train.GradientDescentOptimizer(0.0001).minimize(loss)
train_step = tf.train.AdamOptimizer(0.0001).minimize(loss)

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

init = tf.global_variables_initializer()
sess = tf.InteractiveSession()
sess.run(init)

i = 0
for tmp in pd.read_csv(train_data_path, chunksize=train_size):
    i = i + 1
    temp = np.array(tmp, dtype=np.float32)
    data_train = temp[0:, 0:1024]
    label_train = temp[0:, 1024:]
    train_step.run(feed_dict={x: data_train, labels: label_train})  # trains row by row
    if i % 1 == 0:
        train_accuracy = accuracy.eval(feed_dict={x: data_train, labels: label_train})
        print('accuracy for training data: %.2f' % (train_accuracy * 100), '%')
        i = 0

data_test = np.loadtxt('images.csv', dtype=np.float32, delimiter=',')
test_x = data_test[0:, 0:1024]
test_label = data_test[0:, 1024:]
test_accuracy = accuracy.eval(feed_dict={x: test_x, labels: test_label})
print('accuracy for test data: %.2f' % (test_accuracy * 100), '%')

key = input('do you want to save this result? (y/n):')
if key == 'y':
    model_path = 'model/car_model'
    saver = tf.train.Saver()
    save_path = saver.save(sess, model_path)
    print('model saved')
else: pass