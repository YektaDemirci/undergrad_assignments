# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 18:55:04 2018

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
num_steps = 2000
num_steps2 =8000


# Network Parameters
n_hidden_1 = 8 
n_hidden_2 = 4 
n_hidden_3 = 3 
num_input = 4 
num_classes = 2 

# tf Graph input
X = tf.placeholder("float", [None, num_input])
Y = tf.placeholder("float", [None, num_classes])

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([num_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1,n_hidden_2])),
    'h3': tf.Variable(tf.random_normal([n_hidden_2,n_hidden_3])),
    'out': tf.Variable(tf.random_normal([n_hidden_3, num_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'b3': tf.Variable(tf.random_normal([n_hidden_3])),
    'out': tf.Variable(tf.random_normal([num_classes]))
}

# Create model
def chooser(x,t1,t2,t3):
    if t1 == 1:
        layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['h1']), biases['b1']))
    elif t1 == 2:
        layer_1 = tf.nn.tanh(tf.add(tf.matmul(x, weights['h1']), biases['b1']))
    elif t1 == 3:
        layer_1 = tf.nn.relu(tf.add(tf.matmul(x, weights['h1']), biases['b1']))      
        
    if t2 == 1:
        layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1,weights['h2']),biases['b2']))
    elif t2 == 2:
        layer_2 = tf.nn.tanh(tf.add(tf.matmul(layer_1,weights['h2']),biases['b2']))
    elif t2 == 3:
        layer_2 = tf.nn.relu(tf.add(tf.matmul(layer_1,weights['h2']),biases['b2']))
        
    if t3 == 1:
        layer_3 = tf.nn.sigmoid(tf.add(tf.matmul(layer_2,weights['h3']),biases['b3']))
    elif t3 == 2:
        layer_3 = tf.nn.tanh(tf.add(tf.matmul(layer_2,weights['h3']),biases['b3']))
    elif t3 == 3:
        layer_3 = tf.nn.relu(tf.add(tf.matmul(layer_2,weights['h3']),biases['b3']))
        
    out_layer = tf.matmul(layer_3, weights['out']) + biases['out']
    return out_layer

a=0
b=0
c=0
lr=0
maxall=0.0


for learning_rate in [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]:
    for t1 in range(1,4):
        for t2 in range(1,4):
            for t3 in range(1,4):
                # Construct model
                logits = chooser(X,t1,t2,t3)
                prediction = tf.nn.softmax(logits)
                # Define loss and optimizer
                loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
                logits=logits, labels=Y))
                optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
                train_op = optimizer.minimize(loss_op)
    
                # Evaluate model
                correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
                accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    
                # Initialize the variables (i.e. assign their default value)
                init = tf.global_variables_initializer()
    
                # Start training
                with tf.Session() as sess:
    
                    # Run the initializer
                    sess.run(init)
    
                    for step in range(1, num_steps+1):
                    # Run optimization op (backprop)
                        sess.run(train_op, feed_dict={X: x_train, Y: y_train})
                        if step:
                            # Calculate batch loss and accuracy
                            loss, acc = sess.run([loss_op, accuracy], feed_dict={X: x_train,
                                                                     Y: y_train})
                
                    # Testing
                    temp = sess.run(accuracy, feed_dict={X: x_test,Y: y_test})
                    print("For "+ str(t1)+ " " + str(t2) +" " + str(t3)+ " " + \
                          str(learning_rate) + " " + "Test Accuracy: " + str(temp))
                    if temp> maxall:
                        maxall=temp
                        a=t1
                        b=t2
                        c=t3
                        lr=learning_rate
print(a,b,c,lr)
logits = chooser(X,a,b,c)
prediction = tf.nn.softmax(logits)
# Define loss and optimizer
loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
logits=logits, labels=Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=lr)
train_op = optimizer.minimize(loss_op)

# Evaluate model
correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    for step2 in range(1, num_steps2+1):
        # Run optimization op (backprop)
        sess.run(train_op, feed_dict={X: x_train, Y: y_train})
        if step2:
            # Calculate batch loss and accuracy
            loss, acc = sess.run([loss_op, accuracy], feed_dict={X: x_train,
                                                                 Y: y_train})
           ## print("Epoch " + str(step2) + ", Loss " + \
           ##       "{:.4f}".format(loss))
            plt.scatter(step2, loss,color='blue',marker='.')
    # Testing
    print("Test Accuracy:", \
    sess.run(accuracy, feed_dict={X: x_test,Y: y_test}))
plt.title('Best Combination Loss vs Batch Graph')
plt.xlabel('Epoch numbers')
plt.ylabel('Loss values')
plt.show()