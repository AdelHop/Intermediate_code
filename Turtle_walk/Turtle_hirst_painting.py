import turtle as t
import random

t.colormode(255)
Donatello = t.Turtle()

color_list = [(214, 164, 117),
              (141, 50, 107),
              (165, 170, 38),
              (246, 80, 57),
              (216, 231, 227),
              (68, 199, 219),
              (241, 105, 162),
              (3, 141, 45),
              (230, 236, 240),
              (242, 65, 140),
              (2, 144, 186),
              (19, 166, 127),
              (163, 57, 53),
              (250, 227, 24),
              (163, 174, 168),
              (254, 231, 0),
              (228, 169, 190),
              (32, 192, 214),
              (245, 168, 150),
              (143, 213, 225),
              (170, 204, 184)]


def color_rgb():
    color = random.randint(0, 20)
    r = int(color_list[color][0])
    g = int(color_list[color][1])
    b = int(color_list[color][2])
    rgb = (r, g, b)
    return rgb


level = 0
Donatello.penup()
Donatello.setposition(-200, -200)
Donatello.penup()
Donatello.hideturtle()

for _ in range(10):

    for n in range(10):
        Donatello.dot(20, color_rgb())
        Donatello.forward(50)

    Donatello.setx(-200)
    Donatello.left(90)
    Donatello.forward(50)
    Donatello.right(90)
    level += 1

screen = t.Screen()
screen.exitonclick()
