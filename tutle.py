import turtle
s = turtle.getscreen()
t = turtle.Turtle()
T = turtle.title('Shape maker dumb')
t.pensize(5)
turtle.bgcolor('black')
t.fillcolor("white")
t.pencolor('white')
a = 0
t.begin_fill()
while a <= 2:
    a = int(input('What sided shape? '))
for i in range(1,a+1):
    if a > 5:
        if i%2 == 1:
            t.pencolor('white')
        else:
            t.pencolor('black')
    L = 180*(a-2)
    if a >= 10:
        t.fd(50/(a//10))
    else:
        t.fd(50)
    t.lt(180-(L/a))
t.end_fill()
t.penup()
t.color('black','black')
t.fd(-100)
