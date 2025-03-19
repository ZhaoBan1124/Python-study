num=eval(input("请输入初始存款金额："))
y=eval(input("请输入存款年数："))
result=round(num*(1.05)**y,2)
print("到期总金额：",result)