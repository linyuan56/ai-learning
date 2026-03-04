import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("train.csv", encoding="utf-8")
people1 = 0 # 一号船舱的总数
survived1 = 0 # 一号船舱的存活人数
people2 = 0
survived2 = 0
people3 = 0
survived3 = 0
num = 0 # 行数
for item in df['Pclass']:
    if item == 1:
        people1 += 1
        if df['Survived'].loc[num] == 1:
            survived1 += 1
    elif item == 2:
        people2 += 1
        if df['Survived'].loc[num] == 1:
            survived2 += 1
    else:
        people3 += 1
        if df['Survived'].loc[num] == 1:
            survived3 += 1
    num += 1
# 不同船舱的生还情况的柱状图
# 准备数据
Pclass = ['头等舱', '二等舱', '三等舱']
people = [people1, people2, people3]
survived = [survived1, survived2, survived3]
# 获取每个柱子的坐标
x = np.array(len(Pclass))
# 设置字体为 SimHei (黑体)，Windows 通常自带
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(Pclass, people,0.4, color = 'skyblue')
plt.bar(Pclass, survived,0.4, color = 'blue', alpha = 0.5)
plt.ylabel('人数')
plt.title('泰坦尼克号生还人数和所处船舱等级柱状图对比')

plt.show()
print("这个图很清楚的展示了存活人数随着船舱等级显著上升")