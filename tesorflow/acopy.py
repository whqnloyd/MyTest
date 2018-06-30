import time
import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn
import json

# 创建词汇表,载入数据
with open('data/input.txt', 'r') as f:
    text = f.read()
vocab = set(text)  # 构建字典,建立无序不重复元素集，元素为字母
vocab_size = len(vocab)  # 记录大小
vocab2index = {c: i for i, c in enumerate(vocab)}  # [(a: 0), (b: 1)]
index2vocab = dict(enumerate(vocab))  # [(0：a), (1: b)]
encoded_index = np.array([vocab2index[c] for c in text],
                         dtype=np.int32)  # 文本转数码,[1.0, 2.0, 8.0, 24.0]

'''
vocab2index = {}            # 从字符到位置索引
index2vocab = {}            # 从位置索引到字符
for i, char in enumerate(vocab):
    vocab2index[char] = i
    index2vocab[i] = char

# 词汇保存
def save_vocab(vocab2index, file):
    with open(file, 'w') as f:
        json.dump(vocab2index, 
                  f, indent=2, 
                  sort_keys=True)
'''


# 批量生成
def get_batch(arr, seqs_size, n_seqs):
    batch_size = n_seqs * seqs_size
    n_batch = int(len(arr) / batch_size)
    arr = arr[: batch_size * n_batch]  # 重排，舍弃无法整除的部分
    arr = arr.reshape(n_seqs, -1)  # 以序列个数做分布补充排列
    for n in range(0, arr.shape[1], seqs_size):
        x = arr[: n:n + seqs_size]
        y = np.zeros_like(x)
        y[:, :-1], y[:, -1] = x[:, 1:], y[:, 0]
        yield x, y


# 输入层
def layers_input(seqs_size, n_seqs):
    inputs = tf.placeholder(tf.int32,
                            shape=(seqs_size, n_seqs),
                            name='inputs')
    target = tf.placeholder(tf.int32,
                            shape=(seqs_size, n_seqs),
                            name='targets')
#    keep_prob = tf.placeholder(tf.float32,
#                               name='keep_prob')
    return inputs, target


# LSTM层
# def layers_lstm(lstm_size, keep_prob):
#    lstm = rnn.BasicLSTMCell(lstm_size)
#    drop = rnn.DropoutWrapper(lstm, output_keep_prob=keep_prob)
#    cell = rnn.MultiRNNCell([drop for i in range(n_layers)])
#    initial_state = drop.zero_state(batch_size, tf.float32)
#    return lstm#, initial_state


# 输出层
def layers_output(lstm_output, in_size, out_size):
    seq_output = tf.concat(lstm_output, 1)
    x = tf.reshape(seq_output, [-1, in_size])
    w = tf.Variable(tf.truncated_normal([in_size, out_size], stddev=0.1))
    b = tf.Variable(tf.zeros(shape=[out_size]))
    out = tf.nn.softmax(tf.matmul(x, w) + b, name='predictions')
    return out


# 成本计算
def loss(logits, targets, vocab_size):
    one_hot = tf.one_hot(targets, vocab_size)
    reshaped = tf.reshape(one_hot, logits.get_shape())
    loss = tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=reshaped)
    loss = tf.reduce_mean(loss)
    return loss


# 优化
def optimizer(loss, rate, grad_clip):
    tvars = tf.trainable_variables()
    grads, i = tf.clip_by_average_norm(tf.gradients(loss, tvars), grad_clip)
    train_op = tf.train.AdamOptimizer(rate)
    optimizer = train_op.apply_gradients(zip(grads, tvars))
    return optimizer


seqs_size = 64
n_seqs = 50
lstm_size = 128
learning_rate = 0.01
keep_prob = 1.0
grad_clip = 5
epochs = 20


# 占位符设置
inputs, targets = layers_input(seqs_size, n_seqs)
cell = rnn.BasicLSTMCell(lstm_size)
initial_state = cell.zero_state(seqs_size, tf.float32)
# x_one_hot = tf.one_hot(inputs, vocab_size)
outputs, final_state = tf.nn.dynamic_rnn(cell, inputs, initial_state=initial_state)
y = layers_output(outputs, lstm_size, vocab_size)
loss = loss(y, targets, vocab_size)
optimizer = optimizer(loss, learning_rate, grad_clip)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer)
    for i in range(epochs):
        for x, y in get_batch(encoded_index, seqs_size, n_seqs):
            start = time.time()
            optimizer.run(feed_dict={x: x, y: y})
            end = time.time()
            print(start - end)

'''
class CharRNN:
    def __init__(self,
                 vocab_size,
                 batch_size=64,
                 n_steps=50,
                 lstm_size=128,
                 learning_rate=0.01,
                 grad_clip=5,
                 sampling=False):
        if sampling == True:
            batch_size, n_steps = 1, 1
        else:
            batch_size, n_steps = batch_size, n_steps
        tf.reset_default_graph()
        self.inputs, self.targets, self.keep_prob = layers_input(batch_size, n_steps)
        cell, self.initial_state = layers_lstm(lstm_size, batch_size, self.keep_prob)
        x_one_hot = tf.one_hot(self.inputs, vocab_size)
        outputs, state = tf.nn.dynamic_rnn(cell, x_one_hot, initial_state=self.initial_state)
        self.final_state = state
        self.prediction, self.logits = layers_output(outputs, lstm_size, vocab_size)
        self.loss = loss(self.logits, self.targets, vocab_size)
        self.optimizer = optimizer(self.loss, learning_rate, grad_clip)
'''