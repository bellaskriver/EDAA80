import turtle

ninja = turtle.Turtle()
for i in range(10): # Hur många krävs för att rita en stjärna?
    ninja.forward(50)
    ninja.left(140)
    ninja.forward(50)
    ninja.right(100)

turtle.mainloop()