import turtle
import random

def random_step(t):
    t.forward(random.randint(5, 15))
    if random.randint(0, 1) == 0:
        t.left(45)
    else:
        t.right(45)

def random_walk(t, n):
    for k in range(n):
        random_step(t)

ninja = turtle.Turtle()
random_walk(ninja, 20)

turtle.mainloop()
