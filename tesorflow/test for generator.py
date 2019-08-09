import numpy as np


def get_batch(arr, batch_size):
    n_batch = int(len(arr) / batch_size)
    arr = arr[: batch_size * n_batch]  # 重排，舍弃无法整除的部分
    arr = arr.reshape(n_batch, -1)  # 以序列个数做分布补充排列
    for x in arr:
        yield x

    '''
    for n in range(0, arr.shape[1], seqs_size):
        x = arr[: n:n + seqs_size]
        y = np.zeros_like(x)
        y[:, :-1], y[:, -1] = x[:, 1:], y[:, 0]
        yield x, y
    '''


if __name__ == '__main__':
    with open ('text.txt') as f:
        text = f.read()

    text1 = set(text)
    vocab2index = {}                    # 从字符到位置索引
    index2vocab = {}                    # 从位置索引到字符
    for i, char in enumerate(text1):
        vocab2index[char] = i
        index2vocab[i] = char

    encoded_index = np.array([vocab2index[c] for c in text], dtype=np.int32)  # 文本转数码,[1.0, 2.0, 8.0, 24.0]
    for x in get_batch(encoded_index, 5):
        print(x)
