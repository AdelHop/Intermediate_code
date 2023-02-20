from turtle import Turtle, Screen

Angello = Turtle()
screen = Screen()


def move_forwards():
    Angello.forward(10)


def move_backward():
    Angello.backward(10)


def move_left():
    new_heading = Angello.heading() + 10
    Angello.setheading(new_heading)
    # Angello.left(10)


def move_right():
    new_heading = Angello.heading() - 10
    Angello.setheading(new_heading)
    # Angello.right(10)


def clean_screen():
    Angello.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clean_screen)


screen.exitonclick()
