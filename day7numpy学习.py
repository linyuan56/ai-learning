import numpy as np

matrix = np.arange(12).reshape(3,4)
print(matrix)

print("数组形状", matrix.shape)
print("数据类型", matrix.dtype)
print("数组维度", matrix.ndim)

remake_matrix = matrix.reshape(4,3)
flatted_matrix = matrix.flatten()
print(remake_matrix)
print(flatted_matrix)

print("reshape中-1的用法是自动计算该维度的大小，比如有12个元素的数组，通过matrix.reshape(4, -1)会变成(4, 3)，4的位置是确定的，-1意味着位置是空的，3是由12/4计算出来的")


