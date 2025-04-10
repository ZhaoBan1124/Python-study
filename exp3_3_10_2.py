#画圣诞树方法二
for i in range(1,11):
    for k in range(1,11-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()