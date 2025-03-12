list1=['z','h','o','n','g','h','u','a']
list2=['10',2,'你好']
list3=['10',(1,2,3),[1,2,3]]
print(list1,list2,list3)
print(list1[2],list1[-3:])

list1[2]='e' #修改列表中的单个成员(元素)
list1[0:3]=[1,2,3] #修改列表中的多个成员(元素)
del list1[4:6] #删除列表中的成员(元素)
print(list1)