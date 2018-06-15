import json
import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn


# 创建词汇表
def create_vocab(text):
    vocab = list(set(text))
    print('Words:', vocab)
    size = len(vocab)
    vocab2index = {}            # 从字符到位置索引
    index2vocab = {}            # 从位置索引到字符
    for i, char in enumerate(vocab):
        vocab2index[char] = i
        index2vocab[i] = char
    return vocab2index, index2vocab, size


'''
保存和读取会涉及到编码问题
此处json为排版而设
关于UTF-8请检索codecs模块
'''
# 词汇保存
def save_vocab(vocab2index, file):
    with open(file, 'w') as f:
        json.dump(vocab2index, f, indent=2, sort_keys=True)


# 词汇读取
def load_vocab(file):
    with open(file, 'r') as f:
        vocab2index = json.load(f)
    index2vocab = {}
    size = 0
    for char, index in vocab2index.items():
        index2vocab[index] = char
        size += 1
    return vocab2index, index2vocab, size


# 将文本生成批量训练样本
class BatchGenerator(object):
    def __init__(self, text, batch_size, seq_length, vocab_size, vocab2index):
        self.text = text
        self.text_size = len(text)
        self.batch_size = batch_size
        self.vocab_size = vocab_size
        self.seq_length = seq_length
        self.vocab2index = vocab2index

        segment = self.text_size // batch_size
        self.cursor = [offset * segment for offset in range(batch_size)]
        self.last_batch = self.next_batch()

    def next_batch(self):
        batch = np.zeros(shape=self.batch_size, dtype=np.float)
        for b in range(self.batch_size):
            batch[b] = self.vocab2index[self.text[self.cursor[b]]]
            self.cursor[b] = (self.cursor[b] + 1) % self.text_size
        return batch

    def next(self):
        batches = [self.last_batch]
        for step in range(self.seq_length):
            batches.append(self.next_batch())
        self.last_batch = batches[-1]
        return batches


'''
仅使用基础的RNN
直接实例化一个BasicRNNCell对象
隐含层的神经元数hidden_size
网络的层数rnn_layers
最终用MultiRNNCell封装起来。
'''
# 构建模型
def RNN():
    layer1 = 128
    rnn_layers = 2

    lstm_cell = rnn.BasicRNNCell(layer1)

    cells = [lstm_cell]
    for i in range(rnn_layers - 1):
        higher_layer_cell = lstm_cell(layer1)
        cells.append(higher_layer_cell)
    multi_cell = rnn.BasicRNNCell(cells)

    # 初始化multicell
    self.zero_state = multi_cell.zero_state(self.batch_size, tf.float32)


# 创建占位符，初始状态占位符，输入占位符和输出占位符
def create_tuple_placeholders(inputs, shape):
    if isinstance(shape, int):
        result = tf.placeholder_with_default(inputs, list((None,)) + [shape])
    else:
        sub_placeholders = [create_tuple_placeholders(sub_inputs, sub_shape)
                            for sub_inputs, sub_shape in zip(inputs, shape)]
        t = type(shape)
        if t == tuple:
            result = t(sub_placeholders)
        else:
            result = t(*sub_placeholders)
    return result

self.initial_state = create_tuple_placeholders(multi_cell.zero_state(self.batch_size, tf.float32),
                                               shape=multi_cell.state_size)
self.input_data = tf.placeholder(tf.int64, [self.batch_size, self.seq_length], name='inputs')
self.targets = tf.placeholder(tf.int64, [self.batch_size, self.seq_length], name='targets')

self.embedding = tf.get_variable('embedding', [vocab_size, embedding_size])
inputs = tf.nn.embedding_lookup(self.embedding, self.input_data)