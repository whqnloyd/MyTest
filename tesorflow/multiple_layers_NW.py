import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#载入数据集
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

#设置神经层及个数
layer1 = 400
layer2 = 100
layer3 = 60
layer4 = 30
layer5 = 10

#设置模型
w1 = tf.Variable(tf.zeros([784, layer1]))
b1 = tf.Variable(tf.zeros([layer1]))
w2 = tf.Variable(tf.zeros([layer1, layer2]))
b2 = tf.Variable(tf.zeros([layer2]))
w3 = tf.Variable(tf.zeros([layer2, layer3]))
b3 = tf.Variable(tf.zeros([layer3]))
w4 = tf.Variable(tf.zeros([layer3, layer4]))
b4 = tf.Variable(tf.zeros([layer4]))
w5 = tf.Variable(tf.zeros([layer4, layer5]))
b5 = tf.Variable(tf.zeros([layer5]))

x = tf.placeholder(tf.float32, [None, 784])
y1 = tf.nn.softmax(tf.matmul(x, w1) + b1)
y2 = tf.nn.softmax(tf.matmul(y1, w2) + b2)
y3 = tf.nn.softmax(tf.matmul(y2, w3) + b3)
y4 = tf.nn.softmax(tf.matmul(y3, w4) + b4)
y5 = tf.nn.softmax(tf.matmul(y4, w5) + b5)

labels = tf.placeholder(tf.float32, [None, 10])

#成本评估
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y5, labels=labels))
#loss = - tf.reduce_sum(labels * tf.log(y2))

#梯度下降最小化成本
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

#初始化向量
init = tf.initialize_all_variables()

#设置并启动session
sess = tf.Session()
sess.run(init)

#循环训练
for i in range(5000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, labels: batch_ys})

# 评估
correct_prediction = tf.equal(tf.argmax(y5, 1), tf.argmax(labels, 1))
accu_set = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
correct_rate = sess.run(accu_set, feed_dict={x: mnist.test.images, labels: mnist.test.labels})
print('测试集正确率：%.2f' % (correct_rate * 100), '%')

#保存训练好的模型
model_path = 'model/multiple_layers'
saver = tf.train.Saver()
save_path = saver.save(sess, model_path, global_step=1000)
