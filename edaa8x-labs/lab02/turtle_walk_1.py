import turtle
import random

def random_step(ninja):
    ninja.forward(random.randint(5, 15))
    if random.randint(0, 1) == 0:
        ninja.left(45)
    else:
        ninja.right(45)

def random_walk(ninja, steps):
    for i in range(steps):
        random_step(ninja)

ninja = turtle.Turtle()
random_walk(ninja, 100)

turtle.mainloop()
