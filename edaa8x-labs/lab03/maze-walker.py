import turtle
import maze

# Fråga vilken labyrint som ska användas
n = int(input("Vilken labyrint vill du använda? (1-5): "))

if n == 5:
    turtle.Screen().tracer(2)

m = maze.Maze(n)
t = turtle.Turtle()

turtle.Screen().delay(1)

# Ingångens position
x, y = m.entry()

# Skapa Turtle
t.shape('turtle')
t.shapesize(0.25)
t.color('black')

# Placera Turtle vid ingången
t.penup()
t.goto(x, y)
t.left(90)
t.pendown()

# Algoritm för gång
while not m.at_exit(t.pos()):
    if not m.wall_at_left(t.heading(), t.pos()):
        t.left(90)
        t.forward(1)
    elif not m.wall_in_front(t.heading(), t.pos()):
        t.forward(1)
    else:
        t.right(90)
    
turtle.mainloop()