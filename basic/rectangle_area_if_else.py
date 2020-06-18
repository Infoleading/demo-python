'''
矩形面积计算改进(4)
'''

print("欢迎使用矩形面积计算程序")

parameter = [0.0, 0.0]
for i in range(len(parameter)):
    t = input("请输入矩形一条边长：")
    parameter[i] = float(t)

S = 1
for i in parameter:
    S = S*i

print("矩形的面积为：%f"%S)
