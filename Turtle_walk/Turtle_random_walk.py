import turtle
import random
import turtle as t

Leonardo = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

Leonardo.speed(10)
Leonardo.pensize(10)
direction = [0, 90, 180, 270]

for _ in range(280):
    Leonardo.color(random_color())
    Leonardo.forward(20)
    Leonardo.setheading(random.choice(direction))

# def LeonardoRight():
#     Leonardo.color(random.choice(colors))
#     Leonardo.right(90)
#     Leonardo.forward(20)
#
# def LeonardoLeft():
#     Leonardo.color(random.choice(colors))
#     Leonardo.left(90)
#     Leonardo.forward(20)
#
# while True:
#     choice = random.randint(0,1)
#     if choice == 0:
#         LeonardoRight()
#     else:
#         LeonardoLeft()


screen = t.Screen()
screen.exitonclick()
