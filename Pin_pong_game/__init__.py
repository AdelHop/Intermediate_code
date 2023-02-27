from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PinPong")
screen.tracer(8)


paddle = Paddle()


screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()