w=eval(input('输入体重(kg)：'))
h=eval(input('输入身高(m):'))
bmi=w/h**2
print('你的BMI是：',bmi)
if bmi < 18.5:
    print('过轻')
if 18.5 <= bmi < 25:
    print('正常')
if 25 <= bmi < 30:
    print('超重')
if bmi >= 30:
    print('肥胖')