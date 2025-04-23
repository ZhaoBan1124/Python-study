'''n=16
if n%3 == 0:
    print(f"{n}可以被3整除")
else:
    print(f"{n}不能被3整除")
n=27
if n%3 == 0:
    print(f"{n}可以被3整除")
else:
    print(f"{n}不能被3整除")
n=53
if n%3 == 0:
    print(f"{n}可以被3整除")
else:
    print(f"{n}不能被3整除")
n=78
if n%3 == 0:
    print(f"{n}可以被3整除")
else:
    print(f"{n}不能被3整除")
    '''
########################################################
def zc(n,m):
    if n % m == 0:
        print(f"{n}可以被{m}整除")
    else:
        print(f"{n}不能被{m}整除")
list1=[16,27,53,78,98,67,70]
for i in list1:
    zc(i,3)
    zc(i,5)