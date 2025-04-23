def sxh(n,m):
    sxhlist=[]
    for p in range(n,m):
        i=int(p/100)
        j=int((p-100*i)/10)
        k=int(p%10)
        if p == i**3+j**3+k**3:
            sxhlist.append(p)
    return sxhlist
n=int(input("请输入第一个数："))
m=int(input("请输入第二个数："))
print("{}到{}之间的水仙花数为：{}".format(n,m,sxh(n,m)))