import random
num=random.randint(1,20)
t=0
while t != num:
    t=eval(input("请输入你要猜的数字(1-20)吧:"))
    if t == num:
        print("恭喜！猜对了！")
    elif t < num:
        print("很遗憾！猜的数字偏小了")
    elif t > num:
        print("很遗憾！猜的数字偏大了")