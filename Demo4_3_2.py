import turtle
turtle.color("red","yellow")
turtle.begin_fill()
turtle.hideturtle()
turtle.speed(1)
for i in range(1,21):
    turtle.forward(10*i)
    turtle.right(90)
turtle.end_fill()
turtle.done()
