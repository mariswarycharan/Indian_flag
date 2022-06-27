from re import A
import turtle
import time

t = turtle.Turtle()
a = turtle.Screen()
a.bgcolor("blue")

#t.speed(0)


t.begin_fill()

t.fillcolor("green")



t.forward(160)
t.right(90)
t.forward(40)
t.left(90)
t.forward(-160)
t.right(90)
t.forward(-40)

t.end_fill()

t.begin_fill()


t.fillcolor("white")

t.forward(-40)
t.left(90)
t.forward(160)
t.right(90)
t.forward(40)


t.end_fill()

t.begin_fill()


t.fillcolor("orange")


t.forward(-80)
t.right(90)
t.forward(160)
t.left(90)
t.forward(40)
t.left(90)
t.forward(160)

t.end_fill()

t.backward(80)

t.color("purple")
t.circle(-20)


t.right(90)
t.forward(40)
t.right(90)
t.circle(-20,90)
t.right(90)
t.forward(40)
t.right(90)
t.circle(-20,45)
t.right(90)
t.forward(40)
t.right(90)
t.circle(-20,90)
t.right(90)
t.forward(40)
t.left(90)
t.circle(20,45)

t.color("black")
t.backward(80)

t.begin_fill()
t.fillcolor("red")


t.right(90)
t.forward(250)
t.left(90)
t.forward(70)
t.right(90)
t.forward(40)
t.left(90)
t.forward(70)
t.right(90)
t.forward(40)
t.left(90)
t.forward(70)
t.right(90)
t.forward(40)
t.right(90)

t.forward(420)

t.right(90)
t.forward(40)
t.right(90)
t.forward(70)
t.left(90)
t.forward(40)
t.right(90)
t.forward(70)
t.left(90)
t.forward(40)
t.right(90)
t.forward(70)

t.end_fill()

t.begin_fill()
t.fillcolor("black")

t.backward(5)
t.left(90)
t.forward(330)
t.right(90)
t.forward(5)

t.end_fill()
t.backward(3)

t.begin_fill()
t.fillcolor("red")
t.circle(8)

t.end_fill()





t.hideturtle()













    
    





turtle.mainloop()
