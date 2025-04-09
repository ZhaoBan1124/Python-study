avgScore=0
for i in range(1,16):
    t=eval(input("请输入第"+str(i)+"位同学的成绩:"))
    avgScore=avgScore+t
print("这15位同学的平均分为:",avgScore/15)