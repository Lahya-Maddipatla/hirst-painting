from turtle import *
import random
import time
t=Turtle()
colormode(255)
s=Screen()
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
def game():
    for i in range(5):
        t.penup()
        t.dot(30,random_color())
        t.forward(70)
def start():
    for i in range(2):
        game()
        t.left(90)
        t.forward(70)
        t.left(90)
        t.forward(70)
        game()
        t.right(90)
        t.forward(70)
        t.right(90)
        t.forward(70)
        

start()
s.exitonclick()