import turtle
import random

def random_step(ninja):
    ninja.forward(random.randint(5, 15))
    if random.randint(0, 1) == 0:
        ninja.left(45)
    else:
        ninja.right(45)

turtle.Screen().bgcolor('green')
turtle.Screen().delay(1)

# Turtle 1
t1 = turtle.Turtle()
t1.penup()
t1.goto(-50, -50)
t1.pendown()
t1.shape('turtle')
t1.color('blue')

# Turtle 2
t2 = turtle.Turtle()
t2.penup()
t2.goto(50, 50)
t2.pendown()
t2.shape('turtle')
t2.color('red')

while t1.distance(t2) > 100:
    random_step(t1)
    random_step(t2)

turtle.mainloop()
