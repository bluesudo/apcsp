# James Cooper, October 22 2018, Turtle Lab
from turtle import *

# Setting the view to black
bgcolor("black")
penup()

# Setting the options for the rest of the drawing

setx(-300)
sety(100)
speed(10)
screensize(100,100)
shape("turtle")
color("black")
pencolor("yellow")
penup()
left(90)
forward(100)
right(90)
pendown()

# While loop to create a cool shape
x = 0
while x < 38:
    forward(200)
    right(97)
    forward(50)
    right(120)
    x = x + 1

#Setting new position to make name

#speed(1)
penup()
left(290)
forward(200)
left(90)
backward(100)
right(63)
backward(100)


# Drawing my name
pencolor("blue")
pendown()
forward(130)
penup()

backward(65)
pendown()
right(90)
forward(100)
right(18)
forward(10)
right(18)
forward(10)
right(18)                   # Drawing the letter 'J'
forward(10)
right(18)
forward(10)
right(18)
forward(10)
right(18)
forward(10)
right(18)
forward(10)
right(18)
forward(10)
right(18)
forward(10)
right(18)
forward(10)

penup()
forward(10)                 # Moving to new position for next letter
right(90)
forward(135)

pendown()
forward(40)
right(45)
forward(7)
right(45)
forward(40)
left(45)
forward(7)
right(180)
forward(7)
left(45)                # Drawing the letter 'a'
forward(45)
right(45)
forward(7)
right(45)
forward(35)
right(45)
forward(7)
right(45)

penup()
forward(85)             # Moving to new position for next letter
right(90)

pendown()
forward(50)
backward(40)
right(225)
forward(7)
right(45)
forward(30)             # Drawing the letter 'm'
right(45)
forward(7)
right(45)
forward(40)
right(180)
forward(40)
right(45)
forward(7)
right(45)
forward(30)
right(45)
forward(7)
right(45)
forward(40)

penup()
backward(50)                # Moving to new position for next letter
right(90)
right(180)
forward(35)

pendown()
forward(30)
right(45)
forward(7)
right(45)
forward(20)             
right(45)
forward(7)
right(45)
forward(30)
right(45)
forward(7)
right(45)
forward(20)
right(180)
forward(40)
left(45)                # Drawing the letter 'e'
forward(7)
left(45)
forward(30)
left(45)
forward(7)
left(45)
right(180)
right(45)
forward(7)
right(45)
forward(30)
right(45)
forward(7)
right(45)
forward(40)
right(45)
forward(7)
right(45)

penup()
forward(90)
right(45)               # Moving to new position for next letter
forward(7)
right(45)
right(180)

pendown()
left(45)
forward(7)
left(45)
forward(20)
left(45)
forward(7)
left(45)
forward(15)
left(45)
forward(7)
left(45)
forward(20)             # Drawing the letter 's'
right(45)
forward(7)
right(45)
forward(15)
right(45)
forward(7)
right(45)
forward(20)
right(45)
forward(7)
right(45)

penup()
forward(250)                # Moving to new position
right(90)

pencolor("green")
pendown()
s = 0
while s <=45:               # While loop to create a cool shape
    s = s + 1
    
    forward(60)
    right(70)

penup()
pencolor("red")                # Moving to new position
left(90)
forward(120)

pendown()
forward(50)
right(90)
forward(50)
right(90)               # Drawing a square
forward(50)
right(90)
forward(50)
right(90)

penup()
forward(90)             # Moving to new position
pencolor("white")

pendown()
forward(30)
right(60)
forward(30)
right(60)
forward(30)             # Drawing a hexagon
right(60)
forward(30)
right(60)
forward(30)
right(60)
forward(30)

penup()
forward(100)                # Moving to new position
pencolor("violet")

pendown()
forward(40)
right(120)
forward(40)             # Drawing a triangle
right(120)
forward(40)

penup()
pencolor("black")
forward(100)                # Moving to a new position
left(150)               
forward(50)

# The End
