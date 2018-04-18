import tensorflow as tf

hello = tf.constant("Hello, Tensoflow!")
session = tf.Session()
print(session.run(hello))
