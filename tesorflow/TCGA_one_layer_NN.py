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


# 设置模型
w = tf.Variable(tf.zeros([998, 3]))
b = tf.Variable(tf.zeros([3]))

x = tf.placeholder(tf.float32, [None, 998])
y1 = tf.nn.softmax(tf.matmul(x, w) + b)
labels = tf.placeholder('float', [None, 3])

# 损失函数
loss = -tf.reduce_sum(labels*tf.log(y1))
#loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=y1, labels=labels))        # sum和mean的区别
# 优化器
train_step = tf.train.AdamOptimizer(0.01).minimize(loss)
# 评估模型
correct_prediction = tf.equal(tf.argmax(labels, 1), tf.argmax(y1, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# 初始化向量并启动session
init = tf.global_variables_initializer()
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