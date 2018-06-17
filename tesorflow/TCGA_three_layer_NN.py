import time
import tensorflow as tf

time_start = time.clock()


# 读取下一批数据
def train_batch_x(num):
    sum = []
    with open('data/train_TCGA_x.txt', 'r') as f:
        for i in range(num):
            temp = f.readline()
            temp1 = temp.split('\t')
            temp1 = list(map(float, temp1))
            sum.append(temp1)
    return sum


def train_batch_label(num):
    sum = []
    with open('data/train_TCGA_label.txt', 'r') as f:
        for i in range(num):
            temp = f.readline()
            temp1 = temp.split('\t')
            temp1 = list(map(float, temp1))
            sum.append(temp1)
    return sum


def batch_x_test(num):
    sum = []
    with open('data/test_TCGA_x.txt', 'r') as f:
        for i in range(num):
            temp = f.readline()
            temp1 = temp.split('\t')
            temp1 = list(map(float, temp1))
            sum.append(temp1)
    return sum


def batch_label_test(num):
    sum = []
    with open('data/test_TCGA_label.txt', 'r') as f:
        for i in range(num):
            temp = f.readline()
            temp1 = temp.split('\t')
            temp1 = list(map(float, temp1))
            sum.append(temp1)
    return sum


# 设置输入参数
x = tf.placeholder(tf.float32, [None, 998])
labels = tf.placeholder(tf.float32, [None, 3])


# 权重和偏置
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.zeros(shape=shape)
    return tf.Variable(initial)


# 各层神经元数
layer1 = 100
layer2 = 37
out_layer = 3

# 3层隐藏层
w1 = weight_variable([998, layer1])         # normal配合relu使用，zeros只测试过一层softmax
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
#loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=y3, labels=labels))        # sum和mean的区别
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
for i in range(59):
    batch_size = 3
    train_step.run(feed_dict={x: train_batch_x(batch_size), labels: train_batch_label(batch_size)})
    if i % 9 == 0:
        train_accuracy = accuracy.eval(feed_dict={x: train_batch_x(batch_size), labels: train_batch_label(batch_size)})
        print('训练集准确率：%.2f' % (train_accuracy * 100), '%')
time_end = time.clock()
print('训练时间：%g s' % (time_end - time_start))

# 测试集准确率
test_size = 60
test_accuracy = accuracy.eval(feed_dict={x: batch_x_test(test_size), labels: batch_label_test(test_size)})
print('测试集准确率：%.2f' % (test_accuracy * 100), '%')

'''
# 保存训练好的模型
model_path = 'model/RNN_MNIST'
saver = tf.train.Saver()
save_path = saver.save(sess, model_path, global_step=1000)
'''