import turtle as t
r=100
y=-50
t.speed(0)
for i in range(9):
    t.circle(r)
    t.penup()
    t.goto(0,y)
    t.pendown()
    r=r+50
    y=y-50

t.done()