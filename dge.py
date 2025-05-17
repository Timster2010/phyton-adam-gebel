import turtle

# Set up the screen
turtle.bgcolor("black")  # Set the background color to black

turtle.bgcolor("black")
tina = turtle
tina.shape("turtle")
tina.speed(5)
tina.pensize(3)
tina.pencolor("white")

# Kopf (weiß)
tina.penup()
tina.goto(0, -50)
tina.pendown()
tina.fillcolor("white")
tina.begin_fill()
tina.circle(50)
tina.end_fill()

# Augenbinde (blau)
tina.penup()
tina.goto(-50, 0)
tina.pendown()
tina.pencolor("blue")
tina.fillcolor("blue")
tina.begin_fill()
for _ in range(2):
    tina.forward(100)
    tina.right(90)
    tina.forward(20)
    tina.right(90)
tina.end_fill()

# Körper (schwarz)
tina.penup()
tina.goto(0, -50)
tina.pendown()
tina.pencolor("white")
tina.fillcolor("gray20")
tina.begin_fill()
tina.right(90)
tina.forward(120)
tina.right(90)
tina.forward(40)
tina.right(90)
tina.forward(120)
tina.right(90)
tina.forward(40)
tina.end_fill()

tina.penup()
tina.goto(0, 0)
tina.pendown()

turtle.done()  # Keep the window open