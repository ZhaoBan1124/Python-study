def is_prime(n):
    for i in range(2,n):
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
    return
is_prime(101)