#统计正数、负数、零的个数
x=0 #正数的数量
y=0 #负数的数量
z=0 #零的数量
flag=-1
while True:
    flag = input("请输入一个数字(输入stop停止):")
    if flag == "stop":
        break
    flag = int(flag)
    if flag > 0:
        x=x+1
    elif flag < 0:
        y=y+1
    elif flag == 0:
        z=z+1
print(x)
print(y)
print(z)