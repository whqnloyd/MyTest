import time
import tensorflow as tf

time_start = time.clock()
replace = [0] * 26

# 读取下一批数据
def train_batch_x(num):
    sum = []
    with open('data/train_TCGA_x.txt', 'r') as f:
        for i in range(num):
            temp = f.readline()
            temp1 = temp.split('\t')
            temp1 = list(map(float, temp1))
            temp1.extend(replace)
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
            temp1.extend(replace)
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
x = tf.placeholder(tf.float32, [None, 1024])
x_reshape = tf.reshape(x, [-1, 32, 32, 1])
labels = tf.placeholder(tf.float32, [None, 3])


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
out_layer = 3

# 2层卷积层
w_conv1 = weight_variable([6, 6, 1, layer1])                  # 前两维为patch的大小，输入的通道数目，输出的通道数目（特征数）
b_conv1 = bias_variable([layer1])                             # 每一个输出通道都有一个对应的偏置量
w_conv2 = weight_variable([6, 6, layer1, layer2])
b_conv2 = bias_variable([layer2])

conv1 = tf.nn.relu(convolution(x_reshape, w_conv1) + b_conv1)    # 卷积
pool1 = max_pool(conv1)                                          # 池化
conv2 = tf.nn.relu(convolution(pool1, w_conv2) + b_conv2)
pool2 = max_pool(conv2)

# 密集连接层
w_dc = weight_variable([8 * 8 * layer2, dc_layer])               # 尺寸减小到8x8，加入一个全连接层
b_dc = bias_variable([dc_layer])

pool_flat = tf.reshape(pool2, [-1, 8 * 8 * layer2])
h_fc1 = tf.nn.relu(tf.matmul(pool_flat, w_dc) + b_dc)

# Dropout，减少过拟合,但总感觉没必要，所以调大到0.8，1.0为全输出
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 输出层
w_out = weight_variable([dc_layer, out_layer])
b_out = bias_variable([out_layer])

y = tf.nn.softmax(tf.matmul(h_fc1_drop, w_out) + b_out)

# 成本评估
loss = -tf.reduce_sum(labels*tf.log(y))
# loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=y, labels=labels))        # sum和mean的区别

# 梯度下降最小化成本
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

# 评估模型
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 初始化向量并启动session
init = tf.initialize_all_variables()
sess = tf.InteractiveSession()
sess.run(init)

# 循环训练并评估
for i in range(59):
    batch_size = 3
    train_step.run(feed_dict={x: train_batch_x(batch_size), labels: train_batch_label(batch_size), keep_prob: 1.0})
    if i % 9 == 0:
        train_accuracy = accuracy.eval(feed_dict={x: train_batch_x(batch_size), labels: train_batch_label(batch_size), keep_prob: 1.0})
        print('训练集准确率：%.2f' % (train_accuracy * 100), '%')
time_end = time.clock()
print('训练时间：%g s' % (time_end - time_start))

# 测试集准确率
test_size = 60
test_accuracy = accuracy.eval(feed_dict={x: batch_x_test(test_size), labels: batch_label_test(test_size), keep_prob: 1.0})
print('测试集准确率：%.2f' % (test_accuracy * 100), '%')

'''
# 保存训练好的模型
model_path = 'model/RNN_MNIST'
saver = tf.train.Saver()
save_path = saver.save(sess, model_path, global_step=1000)
'''