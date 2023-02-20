from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "blue", "purple"]

is_race_on = False

# screen dimensions
screen_x = 500
screen_y = 500
screen = Screen()
screen.setup(screen_x, screen_y)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtles = []

# turtle position
x = -230
y = -200

for all_turtle in range(5):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[all_turtle])
    turtle.goto(-230, y + (100 * all_turtle))
    turtles.append(turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            win = turtle.pencolor()
            if win == user_bet:
                print(f"Youve won! The {win} turtle is winner!")
                is_race_on = False
            else:
                print(f"You've lost! The {win} turtle is winner!")
                is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()