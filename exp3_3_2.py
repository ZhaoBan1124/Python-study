list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

s=0
for i in list: #第一种
    s=s+i
print("1至15的累加和为:"+str(s))

s=0
for i in range(1,16): #第二种
    s=s+i
print("1至15的累加和为:"+str(s))