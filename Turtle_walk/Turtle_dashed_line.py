from turtle import Turtle, Screen

# import turtle as t - import ze zmianą nazwy
Leonardo = Turtle()
Leonardo.shape("turtle")
Leonardo.color("red")


def dashed_line(t):
    for i in range(15):
        segment_length = 15
        # dash
        t.forward(segment_length)
        t.penup()
        # skip
        t.forward(segment_length)
        t.pendown()
        # dash
        t.forward(segment_length)


dashed_line(Leonardo)


screen = Screen()
screen.exitonclick()
