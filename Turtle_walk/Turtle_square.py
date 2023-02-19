import turtle

from turtle import Turtle, Screen
Leonardo = Turtle()
Leonardo.shape("turtle")
Leonardo.color("red")

for i in range(0,4):
     Leonardo.forward(100)
     Leonardo.right(90)


screen = Screen()
screen.exitonclick()