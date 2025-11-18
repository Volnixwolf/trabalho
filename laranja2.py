import turtle
import random

t = turtle.Turtle()
tela = turtle.Screen()
tela.setup(width=600, height=600)
tela.title("Clique para desenhar")
t.speed(0)
tamanho_aleatorio = random.randint(50, 300)
t.penup()

def desenhar_no_clique(x, y):
    t.goto(x, y)
    t.pendown()
    t.dot(tamanho_aleatorio, "orange")
    t.penup()

def laranja(tamanho):
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(tamanho)
    t.end_fill()
    t.color("orange")


tela.onscreenclick(desenhar_no_clique,3)

laranja(tamanho_aleatorio)
tela.mainloop()


