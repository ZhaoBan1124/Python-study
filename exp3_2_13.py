a=eval(input('请输入第一条边的长度：'))
b=eval(input('请输入第二条边的长度：'))
c=eval(input('请输入第三条边的长度：'))
if a+b>c and a+c>b and b+c>a:
    print('能组成三角形')
    if a==b or a==c or b==c and a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print('是等腰直角三角形')
    elif a==b or a==c or b==c:
        print('是等腰三角形')
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print('是直角三角形')
else:
    print('不能组成三角形')