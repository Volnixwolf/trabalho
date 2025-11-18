import turtle
import random

t = turtle.Turtle()
tela = turtle.Screen()
tela.setup(width=600, height=600)

t.speed(50)
tamanho_aleatorio = random.randint(1,100)
t.penup()



def desenhar_no_clique(tela):
    """

    """
    t.goto(x, y) 
    t.pendown()
    t.dot(20, "blue") 
    t.penup()


def laranja(tamanho,y):
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(tamanho)
    t.end_fill()
    t.color("orange")


turtle.onscreenclick(laranja,1)

turtle.done()    