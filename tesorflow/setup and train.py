import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("C:/Users/Luodai Yang/PycharmProjects/tensorflow test/MNIST_data/", one_hot=True)

#回归模型 y=softmax(wx+b)
x = tf.placeholder(tf.float32, [None, 784])
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y1 = tf.nn.softmax(tf.matmul(x, w) + b)

#成本评估 y=-multi(y*log(y))
y2 = tf.placeholder('float', [None, 10])
cross_entropy = - tf.reduce_sum(y2 * tf.log(y1))

#梯度下降 速率0.01 最小化成本
train_step=tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#初始化向量
init = tf.initialize_all_variables()

#设置并启动session
sess = tf.Session()
sess.run(init)

#循环训练
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y2: batch_ys})

# 评估
correct_prediction = tf.equal(tf.argmax(y1, 1), tf.argmax(y2, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y2: mnist.test.labels}))

#保存训练好的模型
model_path = "C:/Users/Luodai Yang/PycharmProjects/tensorflow test/model/mymodel"
saver = tf.train.Saver()
save_path = saver.save(sess, model_path, global_step=1000)
