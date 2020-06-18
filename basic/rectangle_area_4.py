'''
矩形面积计算改进(4)
'''

print("欢迎使用矩形面积计算程序")

a = input("请输入矩形长：")
a = float(a)
while a<=0:
    a = input("矩形长必须大于0，请重新输入：")
    a = float(a)

b = input("请输入矩形宽：")
b = float(b)
while b<=0 :
    b = input("矩形宽必须大于0，请重新输入：")
    b = float(b)

S = a*b
print("矩形的面积为：%f"%S)
