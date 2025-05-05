def getAvg(name="",cjs=None):
    print(f'科目名称：{name}')
    if cjs:
        cjmax=0
        cjmin=100
        cjsum=0
        i=0
        for cj in cjs:
            i=i+1
            cjsum=cjsum+cj
            if cj>cjmax:
                cjmax=cj
            if cj<cjmin:
                cjmin=cj
        cjavg=round(cjsum/i,2)
        print(f'最高分是：{cjmax}')
        print(f'最低分是：{cjmin}')
        print(f'平均分是：{cjavg}')
    else:
        print("请输入成绩")
list=[67,89,98,80,63,99,92,81]
print(type(list))
print("语文科目的八个成绩：",list)
getAvg("语文",list)