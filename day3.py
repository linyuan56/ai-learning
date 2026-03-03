message = "Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; Mission:2025-RESCUE-X"
message1 = list(message.split("; "))
# 分隔开来
message2 = message1[2][6:19:]
message3 = set(message2.split(","))
# 完成对重复装备的去重
message4 = message1[3][8:21:]
message5 = message1[1][8:13:]
message6 = tuple(message5.split(","))
print(message5)
# 锁定坐标和截取任务代号
sum = {"Agent":"007_Bond","coords":message6,"Items":message3,"Mission":message4}
print(sum)