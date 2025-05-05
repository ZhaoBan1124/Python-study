def gethobby(name="glc",hobby="编程",*hobbys):
    print(f'{name}喜欢{hobby}')
    if hobbys:
        print(type(hobbys))
        print("除此之外，还喜欢：",end="")
        for i in hobbys:
            print(i,end=",")

#默认参数调用
print("默认值参数调用方式：")
gethobby()
#位置参数调用
print("位置参数调用方式：")
gethobby("szq","打游戏")
#关键字函数调用
print("关键字函数调用方式：")
gethobby(hobby="TG",name="乐乐")
#不定长参数调用
print("不定长参数调用方式：")
gethobby("辰辰","打游戏","喝咖啡","发圈","TG","谈恋爱","焙炒","看史铁生的书","打牌","做咖啡","打羽毛球","旷课","深夜EMO","上课看小说","mnd","怪叫","做表情包","骑自行车","key ring")