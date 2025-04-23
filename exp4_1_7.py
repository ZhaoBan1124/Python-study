def calculate_total(prices,quantities):
    num=0

    for i in range(0,len(prices)):
        price = float(prices[i])
        quantitie=int(quantities[i])
        num += float(price*quantitie)
    return num
prices=input('请输入商品价格(以空格分割):').split()
quantities=input('请输入商品数量(以空格分割):').split()
print(f"总金额：{calculate_total(prices,quantities)}")