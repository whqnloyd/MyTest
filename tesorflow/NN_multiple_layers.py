import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

time_start = time.clock()

# 载入数据集
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# 设置输入参数
x = tf.placeholder(tf.float32, [None, 784])
labels = tf.placeholder(tf.float32, [None, 10])


# 权重和偏置
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.zeros(shape=shape)
    return tf.Variable(initial)


# 各层神经元数
layer1 = 60
layer2 = 30
out_layer = 10

# 3层隐藏层
w1 = weight_variable([784, layer1])         # normal配合relu使用，zeros只测试过一层softmax
b1 = bias_variable([layer1])
w2 = weight_variable([layer1, layer2])
b2 = bias_variable(layer2)
w3 = weight_variable([layer2, out_layer])
b3 = bias_variable([out_layer])

y1 = tf.nn.relu(tf.matmul(x, w1) + b1)             # relu为正则化L1，softplus为正则化L2
y2 = tf.nn.relu(tf.matmul(y1, w2) + b2)
y3 = tf.nn.softmax(tf.matmul(y2, w3) + b3)         # 最后一步使用softmax分配不同类的概率

# 成本评估
loss = -tf.reduce_sum(labels*tf.log(y3))
# loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=y3, labels=labels))        # sum和mean的区别
# 梯度下降最小化成本
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
# 评估模型
correct_prediction = tf.equal(tf.argmax(y3, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 初始化向量并启动session
init = tf.initialize_all_variables()
sess = tf.InteractiveSession()
sess.run(init)

# 循环训练并评估
for i in range(10000):
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
model_path = 'model/NN_multiple_layers'
saver = tf.train.Saver()
save_path = saver.save(sess, model_path, global_step=1000)
