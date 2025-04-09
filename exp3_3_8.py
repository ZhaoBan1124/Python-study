s=0
i=1
n=input("请输入第"+str(i)+"数字:")
while n != "q":
    s=s+float(n)
    i=i+1
    n=input("请输入第"+str(i)+"数字:")
else:
    print(s)