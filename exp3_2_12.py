year = int(input('请输入年份：'))
flag = False
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            flag = True
        else:
            flag = False
    else:
        flag = True
else:
    flag = False

if flag == True:
    print(str(year)+'年是闰年')
else:
    print(str(year) + '年不是闰年')
