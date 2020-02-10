# import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 载入数据集
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# 设置模型  28*28
w = tf.Variable(tf.zeros([784, 10]), name='w')
b = tf.Variable(tf.zeros([10]), name='b')
x = tf.placeholder(tf.float32, [None, 784], name='x')
y = tf.nn.softmax(tf.matmul(x, w) + b, name='y')
labels = tf.placeholder(tf.float32, [None, 10], name='labels')

# 成本评估
loss = - tf.reduce_sum(labels * tf.log(y))
# 梯度下降最小化成本
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
# 准确率计算
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 初始化向量
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# detail_accuracy_train = []
# detail_accuracy_test = []
# x_axis = []
# n = 0

# 循环训练并评估
for i in range(1200):
    batch_x_train, batch_label_train = mnist.train.next_batch(50)
    sess.run(train_step, feed_dict={x: batch_x_train, labels: batch_label_train})
    if i % 50 == 0:
        correct_rate_train = sess.run(accuracy, feed_dict={x: batch_x_train, labels: batch_label_train})
        print('accuracy for train data：%.2f' % (correct_rate_train * 100), '%')

        batch_test = mnist.test.next_batch(1000)
        correct_rate_test = sess.run(accuracy, feed_dict={x: batch_test[0], labels: batch_test[1]})
        print('accuracy for test data：%.2f' % (correct_rate_test * 100), '%')

        # n = n + 1
        # detail_accuracy_train.append(correct_rate_train * 100)
        # detail_accuracy_test.append(correct_rate_test * 100)
        # x_axis.append(n)

# plt.figure()
# plt.plot(x_axis, detail_accuracy_train, color='red')
# plt.plot(x_axis, detail_accuracy_test, color='blue')
# plt.show()

# 保存训练好的模型
model_path = 'model/MNIST'
saver = tf.train.Saver()
save_path = saver.save(sess, model_path)
print('model saved')
