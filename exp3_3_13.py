#生成100以内的质数
for i in range(2,101):
    flag=True
    for j in range(2,i):
        if i%j != 0:
            pass
            continue
        else:
            flag=False
            break
    if flag:
        print(i,end=",")