from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

batch = mnist.train.next_batch(2)

print(batch[0])