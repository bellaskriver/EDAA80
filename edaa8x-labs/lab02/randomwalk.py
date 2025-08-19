import turtle
import random

ninja = turtle.Turtle()
for i in range(4):
    n = random.randint(0, 1)
    if n == 0:
        ninja.right(45)
    else:
        ninja.left(45)
    ninja.forward(10)


turtle.mainloop()