# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 22:32:29 2018

@author: Yekta
"""
# Import data
import pickle
bank = pickle.load(open('/Users/Yekta/Desktop/ODTU2/499/Hw1/Homework1/bank.pkl','rb'))
x_train = bank ['x_train']
y_train = bank ['y_train']
x_test = bank ['x_test']
y_test = bank ['y_test']

import tensorflow as tf
import matplotlib.pyplot as plt

# Parameters
learning_rate = 0.01
num_steps = 4000


# Network Parameters
n_hidden_1 = 4 # 1st layer number of neurons
n_hidden_2 = 3 # 2nd layer number of neurons
num_input = 4 # input number of  neurons
num_classes = 2 # output number of neurons

# tf Graph input
X = tf.placeholder("float", [None, num_input])
Y = tf.placeholder("float", [None, num_classes])

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([num_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1,n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, num_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([num_classes]))
}

# Creating neuron functions
def neural_net(x):
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['h1']), biases['b1']))
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1,weights['h2']),biases['b2']))
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

# Creating hypothesis
logits = neural_net(X)
prediction = tf.nn.softmax(logits)

# Define loss function and optimizing
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=logits, labels=Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss_op)

# Calculating accuracy
correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Training
with tf.Session() as sess:

    # Run the initializer
    sess.run(tf.global_variables_initializer())

    for step in range(1, num_steps+1):
        # Backprop
        sess.run(train_op, feed_dict={X: x_train, Y: y_train})
        if step:
            # Calculate Loss and accuracy
            loss, acc = sess.run([loss_op, accuracy], feed_dict={X: x_train,
                                                                 Y: y_train})
            print("Epoch " + str(step) + ", Loss " + \
                  "{:.4f}".format(loss))
            plt.scatter(step, loss,color='red',marker='.')
    # Testing
    print("Test Accuracy:", \
    sess.run(accuracy, feed_dict={X: x_test,Y: y_test}))
plt.scatter(step, loss,color='green',marker='.')
plt.title('Arch 2 for sigmoid activation function')
plt.xlabel('Epoch numbers')
plt.ylabel('Loss values')
plt.show()