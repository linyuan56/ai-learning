import numpy as np

# 激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([0.0, 0.1, -0.2, 0.3, 0.4]) # 输入
W1 = np.array([0.4, 0.3, -0.7, 0.9, 0.5]) # 权重
b1 = 0.1 # 偏置

# 直接计算法
def neuron1(x, w, b):
    z = 0.0
    for i in range(len(x)):
        z+= x[i]*w[i]
    z += b
    result = sigmoid(z)
    return result

# 矩阵计算
def neuron2(x, w, b):
    return sigmoid(np.dot(x, w) + b)

'''
网络结构:
输入层 (5个节点) -> [权重W1, 偏置b1] -> 隐藏层 (1个神经元)
 -> [权重W2, 偏置b2] -> 输出层 (1个神经元)
 '''
def neuralnetwork(x, w, b):
    a = neuron1(x, w, b)
    W2 = 0.8
    b2 = 0.5
    result = neuron2(a, W2, b2)
    return result