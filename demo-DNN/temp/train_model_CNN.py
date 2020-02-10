import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

time_start = time.clock()

# 载入数据集
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# 设置输入参数
x = tf.placeholder(tf.float32, [None, 784], name='x')
x_reshape = tf.reshape(x, [-1, 28, 28, 1])                  # 第2、第3维为宽、高，最后一维代表图片的颜色通道数(灰度图为1，rgb彩色图为3)
labels = tf.placeholder(tf.float32, [None, 10])


# 权重和偏置
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.zeros(shape=shape)
    return tf.Variable(initial)


# 卷积和池化
def convolution(c_x, c_w):
    return tf.nn.conv2d(c_x, c_w, strides=[1, 1, 1, 1], padding='SAME')


def max_pool(p_x):
    return tf.nn.max_pool(p_x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


# 各层神经元数
layer1 = 32
layer2 = 64
dc_layer = 1024
out_layer = 10

# 2层卷积层
w_conv1 = weight_variable([5, 5, 1, layer1])                  # 前两维为patch的大小，输入的通道数目，输出的通道数目（特征数）
b_conv1 = bias_variable([layer1])                             # 每一个输出通道都有一个对应的偏置量
w_conv2 = weight_variable([5, 5, layer1, layer2])
b_conv2 = bias_variable([layer2])

conv1 = tf.nn.relu(convolution(x_reshape, w_conv1) + b_conv1)    # 卷积
pool1 = max_pool(conv1)                                          # 池化
conv2 = tf.nn.relu(convolution(pool1, w_conv2) + b_conv2)
pool2 = max_pool(conv2)

# 密集连接层
w_dc = weight_variable([7 * 7 * layer2, dc_layer])               # 尺寸减小到7x7，加入一个全连接层
b_dc = bias_variable([dc_layer])

pool_flat = tf.reshape(pool2, [-1, 7 * 7 * layer2])
h_fc1 = tf.nn.relu(tf.matmul(pool_flat, w_dc) + b_dc)

# Dropout，减少过拟合,但总感觉没必要，所以调大到0.8，1.0为全输出
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 输出层
w_out = weight_variable([dc_layer, out_layer])
b_out = bias_variable([out_layer])

y = tf.nn.softmax(tf.matmul(h_fc1_drop, w_out) + b_out, name='y')

# 成本评估
loss = -tf.reduce_sum(labels*tf.log(y))
# loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=y, labels=labels))        # sum和mean的区别

# 梯度下降最小化成本
train_step = tf.train.GradientDescentOptimizer(0.0001).minimize(loss)

# 评估模型
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 初始化向量并启动session
init = tf.initialize_all_variables()
sess = tf.InteractiveSession()
sess.run(init)

# 循环训练
for i in range(12000):
    batch = mnist.train.next_batch(50)                                               # 一共60000个测试样本，每批次在50个时有99.2%的准确率
    train_step.run(feed_dict={x: batch[0], labels: batch[1], keep_prob: 0.5})
    if i % 500 == 0:
        train_accuracy = accuracy.eval(feed_dict={x: batch[0], labels: batch[1], keep_prob: 1.0})
        print('accuracy for tarin data：%.2f' % (train_accuracy * 100), '%')
time_end = time.clock()
print('time for training: %g s' % (time_end - time_start))

# 测试集准确率
batch = mnist.train.next_batch(1000)                # 2GB显卡最大一次载入7000，此测试集有10000样本
test_accuracy = accuracy.eval(feed_dict={x: batch[0], labels: batch[1], keep_prob: 1.0})
print('accuracy for test data：%.2f' % (test_accuracy * 100), '%')

# 保存训练好的模型
model_path = 'model/CNN_MNIST'
saver = tf.train.Saver()
save_path = saver.save(sess, model_path)
