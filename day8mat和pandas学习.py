import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("加州房价数据集.csv", encoding='utf-8', na_values=["", 'nan'])
df_filled = df.copy()
df_filled["total_bedrooms"] = df["total_bedrooms"].fillna(df["total_bedrooms"].median())
# 画出房价与收入的关系
# 设置字体为 SimHei (黑体)，Windows 通常自带
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(df_filled['median_income'], df_filled['median_house_value'], alpha=0.1)
plt.xlabel('收入中位数')
plt.ylabel('房价中位数')
plt.title('收入与房价的关系')
plt.show()

# 画正弦函数
# linspace：在 0 到 10 这个范围内，生成 100 个间隔均匀（等差）的数字
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
plt.plot(x, y1, linestyle='-', label='正弦函数 (sin)')
plt.title("正弦函数")
plt.xlabel('X 轴')
plt.ylabel('Y 轴')
plt.show()
