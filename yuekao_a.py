#!@Author : menglinpan
#!datetime : 2018/8/24 14:02

# 1.	写出求8！的 tensorflow代码。（共8分）
# 创建变量，保存计算结果（3分）
# 初始化变量（2分）
# 执行计算、输出结果（3分）

import tensorflow as tf

n = tf.Variable(1, dtype=tf.float32)

for i in range(8, 1, -1):
    n = tf.multiply(n, float(i))
    #n *= i
sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(n))




