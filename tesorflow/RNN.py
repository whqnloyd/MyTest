import tensorflow as tf
import numpy as np

vocabulary_size = 8000
unknown_token = 'UNKNOWN_TOKEN'
sentence_start_token = 'SENTENCE_START'
sentence_end_token = 'SENTENCE_END'

# 读取数据，添加SENTENCE_START和SENTENCE_END在开头和结尾
print('Reading CSV file...')
with open('data/reddit-comments-2015-08.csv', 'rb') as f:
    reader = csv.reader(f, skipinitialspace=True)
    reader.next()
    sentences = itertools.chain(*[nltk.sent_tokenize(x[0].decode('utf-8').lower()) for x in reader])       # 分句
    sentences = ['%s %s %s' % (sentence_start_token, x, sentence_end_token) for x in sentences]    # 添加SENTENCE_START和SENTENCE_END
print('Parsed %d sentences.' % (len(sentences)))

# 分词
tokenized_sentences = [nltk.word_tokenize(sent) for sent in sentences]

# 统计词频
word_freq = nltk.FreqDist(itertools.chain(*tokenized_sentences))
print('Found %d unique words tokens.' % len(word_freq.items()))

# 取出高频词构建词到位置，和位置到词的索引
vocab = word_freq.most_common(vocabulary_size-1)
index_to_word = [x[0] for x in vocab]
index_to_word.append(unknown_token)
word_to_index = dict([(w,i) for i,w in enumerate(index_to_word)])

print('Using vocabulary size %d.' % vocabulary_size)
print('The least frequent word in our vocabulary is %s and appeared %d times.' % (vocab[-1][0], vocab[-1][1]))

# 把所有词表外的词都标记为unknown_token
for i, sent in enumerate(tokenized_sentences):
    tokenized_sentences[i] = [w if w in word_to_index else unknown_token for w in sent]

print('\nExample sentence: %s' % sentences[0])
print('\nExample sentence after Pre-processing: %s' % tokenized_sentences[0])

# 构建完整训练集
X_train = np.asarray([[word_to_index[w] for w in sent[:-1]] for sent in tokenized_sentences])
y_train = np.asarray([[word_to_index[w] for w in sent[1:]] for sent in tokenized_sentences])

#用以初始化参数
class RNNNumpy:
    def __init__(self, word_dim, hidden_dim=100, bptt_truncate=4):
        # 词表，隐藏层，
        self.word_dim = word_dim
        self.hidden_dim = hidden_dim
        self.bptt_truncate = bptt_truncate

        # 随机初始化参数U,V,W，不能直接把它们都初始化为0,初始化参数为很小的随机数
        self.U = np.random.uniform(-np.sqrt(1./word_dim), np.sqrt(1./word_dim), (hidden_dim, word_dim))
        self.V = np.random.uniform(-np.sqrt(1./hidden_dim), np.sqrt(1./hidden_dim), (word_dim, hidden_dim))
        self.W = np.random.uniform(-np.sqrt(1./hidden_dim), np.sqrt(1./hidden_dim), (hidden_dim, hidden_dim))

#前向计算
def forward_propagation(self, x):
    # 总共的 序列/时间 长度
    T = len(x)
    # 在前向计算时，我们保留所有的时间隐状态s，因为之后会用到
    # 初始的隐状态设为 0
    s = np.zeros((T + 1, self.hidden_dim))
    s[-1] = np.zeros(self.hidden_dim)
    # 在前向计算时，我们也保留所有的时间点输出o，之后也会用到
    o = np.zeros((T, self.word_dim))
    # 每个时间/序列点 进行运算
    for t in np.arange(T):
        # one-hot编码矩阵乘法，可以视作列选择
        s[t] = np.tanh(self.U[:,x[t]] + self.W.dot(s[t-1]))
        o[t] = softmax(self.V.dot(s[t]))
    return [o, s]

RNNNumpy.forward_propagation = forward_propagation

#预测下一个词
def predict(self, x):
    # 做前向计算，取概率最高的词下标
    o, s = self.forward_propagation(x)
    return np.argmax(o, axis=1)

RNNNumpy.predict = predict

#成本计算
def calculate_total_loss(self, x, y):
    L = 0
    # 对于每句话
    for i in np.arange(len(y)):
        o, s = self.forward_propagation(x[i])
        # 我们只在乎预测对的那个词的概率
        correct_word_predictions = o[np.arange(len(y[i])), y[i]]
        # 加到总loss里
        L += -1 * np.sum(np.log(correct_word_predictions))
    return L

def calculate_loss(self, x, y):
    # 除以总样本数
    N = np.sum((len(y_i) for y_i in y))
    return self.calculate_total_loss(x,y)/N

RNNNumpy.calculate_total_loss = calculate_total_loss
RNNNumpy.calculate_loss = calculate_loss


def bptt(self, x, y):
    T = len(y)
    # 反向计算
    o, s = self.forward_propagation(x)
    # We accumulate the gradients in these variables
    dLdU = np.zeros(self.U.shape)
    dLdV = np.zeros(self.V.shape)
    dLdW = np.zeros(self.W.shape)
    delta_o = o
    delta_o[np.arange(len(y)), y] -= 1.
    # For each output backwards...
    for t in np.arange(T)[::-1]:
        dLdV += np.outer(delta_o[t], s[t].T)
        # Initial delta calculation
        delta_t = self.V.T.dot(delta_o[t]) * (1 - (s[t] ** 2))
        # Backpropagation through time (for at most self.bptt_truncate steps)
        for bptt_step in np.arange(max(0, t-self.bptt_truncate), t+1)[::-1]:
            # print "Backpropagation step t=%d bptt step=%d " % (t, bptt_step)
            dLdW += np.outer(delta_t, s[bptt_step-1])
            dLdU[:,x[bptt_step]] += delta_t
            # 每一步更新delta
            delta_t = self.W.T.dot(delta_t) * (1 - s[bptt_step-1] ** 2)
    return [dLdU, dLdV, dLdW]

RNNNumpy.bptt = bptt

# Outer SGD Loop
# - model: The RNN model instance
# - X_train: The training data set
# - y_train: The training data labels
# - learning_rate: Initial learning rate for SGD
# - nepoch: Number of times to iterate through the complete dataset
# - evaluate_loss_after: Evaluate the loss after this many epochs
def train_with_sgd(model, X_train, y_train, learning_rate=0.005, nepoch=100, evaluate_loss_after=5):
    # We keep track of the losses so we can plot them later
    losses = []
    num_examples_seen = 0
    for epoch in range(nepoch):
        # Optionally evaluate the loss
        if (epoch % evaluate_loss_after == 0):
            loss = model.calculate_loss(X_train, y_train)
            losses.append((num_examples_seen, loss))
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print "%s: Loss after num_examples_seen=%d epoch=%d: %f" % (time, num_examples_seen, epoch, loss)
            # Adjust the learning rate if loss increases
            if (len(losses) &gt; 1 and losses[-1][1] &gt; losses[-2][1]):
                learning_rate = learning_rate * 0.5
                print "Setting learning rate to %f" % learning_rate
            sys.stdout.flush()
        # For each training example...
        for i in range(len(y_train)):
            # One SGD step
            model.sgd_step(X_train[i], y_train[i], learning_rate)
            num_examples_seen += 1

from utils import load_model_parameters_theano, save_model_parameters_theano

model = RNNTheano(vocabulary_size, hidden_dim=50)
losses = train_with_sgd(model, X_train, y_train, nepoch=50)
save_model_parameters_theano('./data/trained-model-theano.npz', model)
load_model_parameters_theano('./data/trained-model-theano.npz', model)

def generate_sentence(model):
    # 从 start token/开始符 开始一句话
    new_sentence = [word_to_index[sentence_start_token]]
    # 直到拿到一个 end token/结束符
    while not new_sentence[-1] == word_to_index[sentence_end_token]:
        next_word_probs = model.forward_propagation(new_sentence)
        sampled_word = word_to_index[unknown_token]
        while sampled_word == word_to_index[unknown_token]:
            samples = np.random.multinomial(1, next_word_probs[-1])
            sampled_word = np.argmax(samples)
        new_sentence.append(sampled_word)
    sentence_str = [index_to_word[x] for x in new_sentence[1:-1]]
    return sentence_str

num_sentences = 10
senten_min_length = 7

for i in range(num_sentences):
    sent = []
    # 短句就不要咯，留下长的就好
    while len(sent) &lt; senten_min_length:
        sent = generate_sentence(model)
    print " ".join(sent)