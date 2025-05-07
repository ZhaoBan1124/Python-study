import math

#########exp4_2_1#########
# scores=[34,23,45,67,98,79,90,100,99,45,87,89,88]
# fsd=[0,0,0,0,0,0]
# fsd_name=["60以下","60到70之间","70到80之间","80到90之间","90到100之间","100分"]
# print("成绩最高分是：",max(scores))
# print("成绩最低分是：",min(scores))
# print("成绩两级差是：",max(scores)-min(scores))
# print("成绩平均分是：",round(sum(scores)/len(scores),2))
# for i in scores:
#     if i<60:
#         fsd[0] += 1
#     elif 60<=i<70:
#         fsd[1] += 1
#     elif 70<=i<80:
#         fsd[2] += 1
#     elif 80<=i<90:
#         fsd[3] += 1
#     elif 90<=i<100:
#         fsd[4] += 1
#     else:
#         fsd[5] += 1
# for i in range(0,len(fsd)):
#     print("{0}的人数为{1}".format(fsd_name[i],fsd[i]))

#########思考题#########
def hanshu(a,b,c):
    global x
    global x1
    global x2
    if b**2-4*a*c >= 0:
        x1=(-b+math.sqrt(b**2-4*a*c))/2*a
        x2=(-b-math.sqrt(b**2-4*a*c))/2*a
        return x1,x2
    elif b**2-4*a*c == 0:
        x=-b/2*a
        return x
    else:
        x="无实数根"
        return x

x=-1
x1=-1
x2=-1

hanshu(4,8,1)
if x == -1:
    print(f"函数的一个根为{x1}")
    print(f"函数的另一个根为{x2}")
else:
    print(f"函数的根为{x}")