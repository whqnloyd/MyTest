import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 载入数据集
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# 设置模型
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

x = tf.placeholder(tf.float32, [None, 784])
y1 = tf.nn.softmax(tf.matmul(x, w) + b)
labels = tf.placeholder('float', [None, 10])

# 成本评估
cross_entropy = - tf.reduce_sum(labels * tf.log(y1))

# 梯度下降最小化成本
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# 初始化向量
init = tf.initialize_all_variables()

# 设置并启动session
sess = tf.Session()
sess.run(init)

# 循环训练并评估
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(60)
    sess.run(train_step, feed_dict={x: batch_xs, labels: batch_ys})
    if i % 100 == 0:
        correct_prediction = tf.equal(tf.argmax(y1, 1), tf.argmax(labels, 1))
        accu_set = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        correct_rate = sess.run(accu_set, feed_dict={x: mnist.test.images, labels: mnist.test.labels})
        print('测试集准确率：%.2f' % (correct_rate * 100), '%')

# 保存训练好的模型
model_path = 'model/NN_one_layer'
saver = tf.train.Saver()
save_path = saver.save(sess, model_path, global_step=1000)
