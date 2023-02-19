import turtle

from turtle import Turtle, Screen
# import turtle as t - import ze zmianą nazwy
Leonardo = Turtle()
Leonardo.shape("turtle")
Leonardo.color("red")

colors = ["yellow", "gold", "dark goldenrod", "firebrick", "dark red", "dark slate blue", "cornflower blue", "medium blue", "medium spring green", "dark green"]

n = 3

while n < 10:
    for i in range(n):
        Leonardo.pencolor(colors[n - 3])
        Leonardo.forward(100)
        Leonardo.right(360/n)

    n +=1











screen = Screen()
screen.exitonclick()