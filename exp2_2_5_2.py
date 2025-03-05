num = float(input('请输入购物金额：'))

if num >= 100 and num < 200:
    print(0.9 * num)
elif num >= 200:
    print(0.8 * num)
else:
    print(num)