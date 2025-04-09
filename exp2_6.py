id = str(input("请输入你的身份证号码："))
y = id[6:10]
m = id[10:12]
d = id[12:14]
sheng_xiao = ['鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪']
sx = int((int(y)-4)%12)
sx = int(sx)
nian_lin = 2025-int(y)-1
xing_bie = int(id[16:17]) % 2
print("您的生日为：",y,"年",m,"月",d,"日")
if xing_bie == 1:
    print("您的性别为：男")
else:
    print("您的性别为：女")
print("您的年龄为：",nian_lin)
print("您属：",sheng_xiao[sx])