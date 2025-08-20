import turtle
import maze
# Skapa ett Maze-objekt och ladda labyrint 1
lab = maze.Maze(1)

# Skapa en sköldpadda och placera den vid ingången av labyrinten
t = turtle.Turtle()
t.penup()  # Ta upp pennan så att den inte ritar när vi flyttar till startpositionen

# Hämta ingångspositionen från labyrinten
start_x, start_y = lab.entrance

# Flytta sköldpaddan till ingångspositionen
t.goto(start_x, start_y)

# Sätt riktningen uppåt (90 grader)
t.setheading(90)

t.pendown()  # Sätt ner pennan

# Visa labyrinten
# Fråga användaren vilken labyrint som ska användas
lab_num = int(turtle.numinput("Labyrintval", "Vilken labyrint vill du använda? (1-5)", minval=1, maxval=5))
lab = maze.Maze(lab_num)

# Om labyrint 5, minska fördröjningen och öka tracer
if lab_num == 5:
    turtle.delay(1)
    turtle.Screen().tracer(2)

# Skapa en sköldpadda och placera den vid ingången av labyrinten
t = turtle.Turtle(shape='turtle')
t.shapesize(0.25)  # Minska storleken till 25%
t.penup()

start_x, start_y = lab.entrance
t.goto(start_x, start_y)
t.setheading(90)
t.pendown()

# Visa labyrinten
turtle.mainloop()
