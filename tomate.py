import turtle
import random
t = turtle.Turtle()


turtle.Screen().screensize(600,500)
t.speed(1)
tamanho =random.randint(50,100)


t.fillcolor("red")
t.begin_fill()
t.circle(50)
t.end_fill()
t.color("red")
t.left(90)
t.forward(100)
t.color("green")
t.pensize(5)
t.forward(20)
t.backward(20)
t.left(45)
t.forward(25)
t.left(25)
t.forward(25)
t.backward(25)
t.right(25)
t.backward(25)
t.left(35)
t.forward(25)
t.left(45)
t.forward(25)
t.backward(25)
t.right(45)
t.backward(25)
t.right(115)
t.forward(25)
t.right(45)
t.forward(25)
t.backward(25)
t.left(45)
t.backward(25)
t.right(45)
t.forward(25)
t.right(35)
t.forward(25)




turtle.done()