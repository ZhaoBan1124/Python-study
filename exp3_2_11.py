time=eval(input('请输入使用时间：'))
if time>=30:
    print('停止使用')
elif time<10:
    print('可继续使用')
else:
    x=str(input('是否继续使用(Y/N)?'))
    if x=='Y':
        print('允许继续使用')
    elif x=='N':
        print('即将终止使用')