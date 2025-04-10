#冒泡排序的实现方式
list=[23,12,9,15,6]
n=len(list)
for i in range(n):
    for j in range(0,n-1-i):
        if list[j] > list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print("排序后的数组:",list)