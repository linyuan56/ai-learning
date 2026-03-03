import json
import math # 提供math.isfinite()函数

# 推导式完成输出平方数
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [number** 2 for number in list1]
print(list2)
# 完成map的习题
list3 = ["张三","李四"]
list4 = map(lambda item: "QG_"+item, list3)
print(list(list4))
# 完成数据筛选的任务
def filtering(obj):
    # 参考过ai的方案，自己改了改
    filtered_data = []
    if isinstance(obj, list):
        for item in obj:
            filtered_data.extend(filtering(item))
    elif isinstance(obj, dict):
        for item in obj.values():
            filtered_data.extend(filtering(item))
    else:
    # 其实这个在这里斌没用，我还想着能不能把列表中的元素挨个提出来，但是好像我现在还做不到
        try:
            filtered_data.append(obj)
        except ValueError:
            pass
    return filtered_data

def is_number(obj):
    data = []
    for item in obj:
        try:
            if item is not None and math.isfinite(float(item)) and float(item) > 80:
                data.append(float(item))
        except ValueError:
            pass
    return data

with open('energy_data.json',"r",encoding="UTF-8") as f:
    raw_data = json.load(f)
    half_raw_data = filtering(raw_data)
    data = is_number(half_raw_data)
max = data[0]
min = data[0]
for item in data:
    if item > max:
        max = item
    elif item < min:
        min = item
number = 0
for item in data:
    number += (item-min)/(max-min)
print(number)