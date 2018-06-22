from RNN_test2 import CharRNN

batch_size = 100
n_steps = 100
lstm_size = 512
n_layers = 2
learning_rate = 0.01
keep_prob = 0.5


epochs = 20
model = CharRNN(len(vocab),
                batch_size=batch_size,
                n_steps=n_steps,
                lstm_size=lstm_size,
                n_layers=n_layers,
                learning_rate=learning_rate,
                grad_clip=5,
                sampling=False)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer)
    counter = 0
    for e in range(epochs):
        new_state = sess.run(model.initial_state)
        loss = 0
        for x, y in get_batch(encoded, batch_size, n_steps):
            counter += 1
            start = time.time()
            feed = {model.inputs: x,
                    model.targets: y,
                    model.keep_prob: keep_prob,
                    model.initial_state: new_state}
            batch_loss, new_state, i = sess.run([model.loss,
                                                model.final_state,
                                                model.optimizer],
                                                feed_dict=feed)
            end = time.time()