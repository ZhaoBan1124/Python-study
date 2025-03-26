pay=eval(input('请输入月收入：'))
pay2=pay-5000
if pay2<=0:
    tax=0
elif pay2<3000:
    tax=pay2*0.03-0
elif pay2<12000:
    tax=pay2*0.1-210
elif pay2<25000:
    tax=pay2*0.2-1410
elif pay2<35000:
    tax=pay2*0.25-2660
elif pay2<55000:
    tax=pay2*0.3-4410
elif pay2<80000:
    tax=pay2*0.35-7160
else:
    tax=pay2*0.45-15160
print('扣税：'+str(tax))
print('税后收入:'+str(pay-tax))