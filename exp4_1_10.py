def f(s):
    s2=""
    for i in s:#12345678
        s2=i+s2 #1,21,321,4321,54321 上海自来水来自海上
    if s==s2:
        return "回文"
    else:
        return "不是回文"

while True:
    s=input("请输入一串字符串(-1退出)：")
    if s==-1:
        break
    else:
        print(s,f(s))