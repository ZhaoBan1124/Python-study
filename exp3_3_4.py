#小练习：利用for循环求1-2+3-4+5-......+99-100的值
a=0
for i in range(1,101,2):
    a=a+i
for i in range(2,101,2):
    a=a-i
print(a)