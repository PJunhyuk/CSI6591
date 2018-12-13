import tensorflow as tf
import numpy as np

x_data = np.array([
    [0,2,4,5,12,13],
    [3,6,7,9,10,12],
    [0,1,5,6,8,12],
    [0,1,5,6,9,13],
    [0,5,9,12,13,14],
    [3,5,6,8,11,13],
    [0,1,2,3,4,5],
    [0,1,2,3,4,6],
    [1,3,4,7,11,13],
    [1,2,3,4,11,13],
    [1,4,5,6,10,13],
    [1,4,5,6,13,14],
    [3,4,6,9,10,11],
    [1,3,5,9,10,13],
    [1,3,5,10,11,13],
    [0,1,4,5,6,12],
    [0,1,4,5,6,13],
    [9,10,11,12,13,14]
    ######
])

y_data = np.array([
    [0,0,1],
    [0,0,1],
    [0,1,0],
    [0,0,1],
    [0,0,1],
    [0,0,1],
    [1,0,0],
    [1,0,0],
    [0,0,1],
    [0,0,1],
    [0,1,0],
    [0,0,1],
    [0,1,0],
    [0,1,0],
    [0,0,1],
    [1,0,0],
    [0,0,1],
    [0,1,0]
])¡

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_uniform([6, 3], -1., 1.))

b = tf.Variable(tf.zeros([3]))

L = tf.add(tf.matmul(X, W), b)
L = tf.nn.relu(L)

model = tf.nn.softmax(L)

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(model), axis=1))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(cost)


init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(3000):
    sess.run(train_op, feed_dict={X: x_data, Y: y_data})

    if (step + 1) % 10 == 0:
        print(step + 1, sess.run(cost, feed_dict={X: x_data, Y: y_data}))


prediction = tf.argmax(model, 1)
target = tf.argmax(Y, 1)
print('예측값:', sess.run(prediction, feed_dict={X: x_data}))
print('실제값:', sess.run(target, feed_dict={Y: y_data}))

is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도: %.2f' % sess.run(accuracy * 100, feed_dict={X: x_data, Y: y_data}))

print('[0,2,4,5,12,13]:', sess.run(model, feed_dict={X: np.array([[0,2,4,5,12,13]])}))
