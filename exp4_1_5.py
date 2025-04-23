n=int(input('请输入n值:'))
def cfb(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(f"{j}*{i}={j*i}",end="\t")
        print()
cfb(n)