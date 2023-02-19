import random
import turtle as t

Leonardo = t.Turtle()
t.colormode(255)
Leonardo.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def circle():
    Leonardo.position()
    Leonardo.heading()
    Leonardo.circle(50)
    Leonardo.position()
    Leonardo.heading()


def spirograph(size_gap):
    for _ in range(int(360 / size_gap)):
        Leonardo.color(random_color())
        circle()
        Leonardo.right(size_gap)


spirograph(60)


screen = t.Screen()
screen.exitonclick()