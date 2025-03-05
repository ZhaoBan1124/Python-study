num1 = float(input('请输入一个数字：'))
num2 = float(input('请输入一个数字：'))
if num1 > num2:
    print('较大的数字：',num1)
    print('较小的数字：',num2)
    print('是否相等：', num1 == num2)
elif num1 < num2:
    print('较大的数字：', num2)
    print('较小的数字：', num1)
    print('是否相等：', num1 == num2)
else:
    print('是否相等：', num1 == num2)