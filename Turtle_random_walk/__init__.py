import turtle

from turtle import Turtle, Screen
# import turtle as t - import ze zmianą nazwy
Leonardo = Turtle()
Leonardo.shape("turtle")
Leonardo.color("red")

# simple squer
# for i in range(0,4):
#     Leonardo.forward(100)
#     Leonardo.right(90)

# def dashed_line(t):
#     for i in range(15):
#         segment_length = 15
#         # dash
#         t.forward(segment_length)
#         t.penup()
#         # skip
#         t.forward(segment_length)
#         t.pendown()
#         # dash
#         t.forward(segment_length)
#
# dashed_line(Leonardo)

# colors = ["yellow", "gold", "dark goldenrod", "firebrick", "dark red", "dark slate blue", "cornflower blue", "medium blue", "medium spring green", "dark green"]
#
# n = 3
#
# while n < 10:
#     for i in range(n):
#         Leonardo.pencolor(colors[n - 3])
#         Leonardo.forward(100)
#         Leonardo.right(360/n)
#
#     n +=1











screen = Screen()
screen.exitonclick()