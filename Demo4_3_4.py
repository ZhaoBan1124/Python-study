import turtle

# 设置画布
screen = turtle.Screen()
screen.title("奥运五环")
screen.bgcolor("white")

# 创建画笔
pen = turtle.Turtle()
pen.width(5)  # 设置线条宽度

# 五环颜色
colors = ["blue", "black", "red", "yellow", "green"]

# 五环位置
positions = [(-110, 0), (0, 0), (110, 0), (-55, -50), (55, -50)]

# 绘制五环
for color, pos in zip(colors, positions):
    pen.penup()
    pen.goto(pos)
    pen.pendown()
    pen.color(color)
    pen.circle(50)

# 隐藏画笔
pen.hideturtle()

# 保持窗口打开
turtle.done()