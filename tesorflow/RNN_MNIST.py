'''
长短时记忆网络（LSTM）是为了解决在复杂的场景中，有用信息的间隔有大有小、长短不一的问题
LSTM是一种拥有三个门结构的特殊网络结构。
'''

import time
import tensorflow as tf
from tensorflow.contrib import rnn
from tensorflow.examples.tutorials.mnist import input_data

time_start = time.clock()

# 载入数据集
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

# 设置输入参数
x = tf.placeholder(tf.float32, [None, 784])
x_reshape = tf.reshape(x, [-1, 28, 28])
labels = tf.placeholder(tf.float32, [None, 10])

# 单层
layer1 = 128
#n_layers = 2
out_layer = 10

# 自带有一个dropout
lstm_cell = rnn.BasicLSTMCell(layer1, forget_bias=1.0)
#cell = rnn.MultiRNNCell([lstm_cell for i in range(n_layers)])

# 处理变长文本，减少计算量，也是一次执行多步，多次调用call
outputs, final_state = tf.nn.dynamic_rnn(lstm_cell, x_reshape, dtype=tf.float32)

# 由于需要处理分类问题，所以需要softmax做处理
w = tf.Variable(tf.truncated_normal([layer1, out_layer], stddev=0.1))
b = tf.Variable(tf.zeros(shape=[out_layer]))

y = tf.nn.softmax(tf.matmul(final_state[1], w) + b)

# 损失函数
loss = -tf.reduce_sum(labels*tf.log(y))
# 优化器
train_step = tf.train.AdamOptimizer(0.01).minimize(loss)
# 评估模型
correct_prediction = tf.equal(tf.argmax(labels, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# 初始化向量并启动session
init = tf.global_variables_initializer()
sess = tf.InteractiveSession()
sess.run(init)

# 循环训练并评估
for i in range(5000):
    batch = mnist.train.next_batch(6)
    train_step.run(feed_dict={x: batch[0], labels: batch[1]})
    if i % 1000 == 0:
        train_accuracy = accuracy.eval(feed_dict={x: batch[0], labels: batch[1]})
        print('训练集准确率：%.2f' % (train_accuracy * 100), '%')
time_end = time.clock()
print('训练时间：%g s' % (time_end - time_start))

# 测试集准确率
batch = mnist.train.next_batch(1000)                # 2GB显卡最大一次载入7000，此测试集有10000样本
test_accuracy = accuracy.eval(feed_dict={x: batch[0], labels: batch[1]})
print('测试集准确率：%.2f' % (test_accuracy * 100), '%')

# 保存训练好的模型
model_path = 'model/RNN_MNIST'
saver = tf.train.Saver()
save_path = saver.save(sess, model_path, global_step=1000)
