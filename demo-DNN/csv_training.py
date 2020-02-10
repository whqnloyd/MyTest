import pandas as pd
import numpy as np
import tensorflow as tf

train_data_path = 'training_data.csv'
train_size = 100

# setup the model
w = tf.Variable(tf.zeros([64*2*48*2, 3]))
b = tf.Variable(tf.zeros([3]))

x = tf.placeholder(tf.float32, [None, 64*2*48*2], name='x')
y = tf.nn.softmax(tf.matmul(x, w) + b, name='y')
labels = tf.placeholder('float', [None, 3])

# loss
loss = -tf.reduce_sum(labels*tf.log(y))
# optimizer
train_step = tf.train.AdamOptimizer(0.01).minimize(loss)
# evaluation
correct_prediction = tf.equal(tf.argmax(labels, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# session
init = tf.global_variables_initializer()
sess = tf.InteractiveSession()
sess.run(init)

i = 0
# read next batch and training
for tmp in pd.read_csv(train_data_path, chunksize=train_size):
    i = i + 1
    temp = np.array(tmp, dtype=np.float32)
    data_train = temp[0:, 0:4]
    label_train = temp[0:, 4:]
    train_step.run(feed_dict={x: data_train, labels: label_train})
    if i % 5 == 0:
        train_accuracy = accuracy.eval(feed_dict={x: data_train, labels: label_train})
        print('accuracy for training data: %.2f' % (train_accuracy * 100), '%')
        i = 0

# accuracy for test data
data_test = np.loadtxt('test_data.csv', dtype=np.float32, delimiter=',')
test_x = data_test[0:, 0:4]
test_label = data_test[0:, 4:]
test_accuracy = accuracy.eval(feed_dict={x: test_x, labels: test_label})
print('accuracy for test data: %.2f' % (test_accuracy * 100), '%')

# save the trained model
model_path = 'model/stock_model'
saver = tf.train.Saver()
save_path = saver.save(sess, model_path, global_step=100)