def calculate_total(prices,quantities):
    print(len(prices))
    print(len(quantities))
    num=0
    for i in range(0,len(prices)):
        num += eval(prices[i]*eval(quantities[i]))
    return num

prices=input('请输入商品价格(以空格分割):').split()
quantities=input('请输入商品数量(以空格分割):').split()
print(calculate_total(prices,quantities))