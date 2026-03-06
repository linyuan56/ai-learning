import numpy as np
import pandas as pd
# 实不相瞒，很多抄的ai，很多函数我一开始都不知道是啥。
# 只能说ai的确实知道的多，我尝试追上ai步伐并已经理解我在这个文件上打的每一行代码的用处

def wash_data():
    # 清洗操作
    column_names = [
        'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
        'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'
    ]
    # 只在下面这行用一下pd，不想再冥思苦想了
    df = pd.read_csv("波士顿房价.csv", sep = "\s+", header = None, names = column_names)
    print("前五行数据\n",df.head())
    # 分离X和Y
    X = df.drop('MEDV', axis = 1) # drop代表删除，axis = 1代表删除列，=0就删除行
    Y = df['MEDV']
    # 分离训练和测验，抄ai的，真不会(流泪……)
    np.random.seed(2026) # 生成随机数（括号内的数随便）
    n_sample = X.shape[0] # 查看X的第一列长度
    indices = np.arange(n_sample) # 生成该长度的一维数组
    np.random.shuffle(indices) # 打乱该数组，实现随机
    split = int(n_sample * 0.8) # 分割点，实现训练组和测验组的比例是4:1
    # 先划分再归一化：用训练集的min/max归一化测试集
    X_train = X.iloc[indices[:split]]
    X_test = X.iloc[indices[split:]]
    y_train = Y.iloc[indices[:split]]
    y_test = Y.iloc[indices[split:]]
    # 用训练集的min/max归一化
    min_vals = np.min(X_train, axis=0)
    max_vals = np.max(X_train, axis=0)
    X_train_normalized = (X_train - min_vals) / (max_vals - min_vals)
    X_test_normalized = (X_test - min_vals) / (max_vals - min_vals)
    return X_train_normalized, y_train, X_test_normalized, y_test

def Normalization(X):
    # 数据归一化操作
    min_vals = np.min(X, axis = 0) # 按列求最小值
    max_vals = np.max(X, axis = 0)
    range_vals = max_vals - min_vals # 每列极差
    X_normalized = (X - min_vals) / range_vals
    return X_normalized

# 1. 为什么要在__init__中设置w和b，在fit函数中不是更好吗
class LinearRegressionNumpy:
    # 抄ai的，自己尝试理解了一下
    def __init__(self):
        self.W = None # 权重w
        self.b= None # 偏置b

    def fit(self, X, y):
        '''
        使用正规方程 (Normal Equation) 求解
        theta = (X^T * X)^(-1) * X^T * y
        一步到位，不需要像梯度下降法一样折磨
        '''

        # 添加偏置列
        ones = np.ones((X.shape[0], 1))
        X_b = np.hstack((ones, X))

        # 计算 thetha
        theta = np.linalg.pinv(X_b.T.dot(X_b)).dot(X_b.T).dot(y) # 2. np.linalg.pinv是什么函数，为什么更稳定

        self.b = theta[0]
        self.W = theta[1:]
        return self # 3. 为什么return self，self是什么

    def predict(self, X):
        return np.dot(X, self.W) + self.b # 进行预测

if __name__ == "__main__":
    # 数据处理
    X_train, y_train, X_test, y_test = wash_data()
    # 训练模型
    model = LinearRegressionNumpy()
    model.fit(X_train, y_train)
    # 评估环节
    y_test_predict = model.predict(X_test)
    MSE = np.mean((y_test - y_test_predict)**2)
    print(f"MSE: {MSE:.4f}")

class LinearRegression:
    def __init__(self, learning_rate = 0.01, iterations = 10000):
        # 4. 设置在self后面是代表可以进行调整吗？
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.W = None
        self.b = None

    def fit(self, X, y):
        X = X.values
        y = y.values
        n_samples,n_features = X.shape # 通过序列解包去赋予值
        self.W = np.random.randn(n_features) # 使用randn生成正态分布随机数（围绕0对称且数值较小）
        self.b = 0.0 # 初始一般为0。np.random.randn(shape) 接收一个表示 形状 的元组（tuple）

        # 开始迭代
        for i in range(self.iterations):
            # 前向传播
            y_predict = np.dot(X, self.W) + self.b
            # 计算误差
            error = y - y_predict
            # 求w和b的梯度
            dw = (1 / n_samples) * np.dot(X.T, error)
            db = (1 / n_samples) * np.sum(error)
            # 更新数据
            self.W += self.learning_rate * dw # 5. 为什么这边反而要加 6. 为什么这边的w和b是这样设计的
            self.b += self.learning_rate * db
        return self

    def predict(self, X):
        return np.dot(X, self.W) + self.b

if __name__ == "__main__":
    X_train, y_train, X_test, y_test = wash_data()
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_test_predict = model.predict(X_test)
    MSE = np.mean((y_test - y_test_predict)**2)
    print(f"MSE: {MSE:.4f}")