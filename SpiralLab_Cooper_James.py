# James Cooper, October 25 2018, Spiral Lab
from turtle import *

bgcolor("Black")            # Setting color of drawing area to black
def square(x):              # Defining square shape
    pencolor("yellow")
    for i in range(1,5):
        forward(x)
        right(90)

def triangle(x):            # Defining triangle shape
    pencolor("blue")
    for i in range(1,4):
        forward(x)
        right(120)

def hexagon(x):             # Defining hexagon shape
    pencolor("red")
    for i in range(1,7):
        forward(x)
        right(60)

def octagon(x):             # Defining octagon shape
    pencolor("violet")
    for i in range(1,9):
        forward(x)
        right(45)

def pentagon(x):            # Defining pentagon shape
    pencolor("green") 
    for i in range(1,6):
        forward(x)
        right(72)

def spiralls():             # Defining spiral loop for square
    for i in range(1,31):
        square(50)
        right(15)

def spirallt():             # Defining spiral loop for triangle
    for i in range(1,31):
        triangle(55) 
        right(15)

def spirallh():             # Defining spiral loop for hexagon
    for i in range(1,31):
        hexagon(40) 
        right(15)

def spirallo():             # Defining spiral loop for octagon
    for i in range(1,31):
        octagon(40) 
        right(15)

def spirallp():             # Defining spiral loop for pentagon
    for i in range(1,31):
        pentagon(50)
        right(15)


color('black')              # Setting turtle inside color to black
speed(10)                   # Setting turtle speed to 10

spirallh()                  # Calls spirallh function to draw a hexagon spiral
penup()

right(90)                   # Moving to new position for next shape
forward(180)

pendown()
spirallt()                  # Calls spirallt function to draw a triangle spiral
penup()

right(90)                   # Moving to new position for next shape
forward(365)

pendown()
spiralls()                  # Calls spiralls function to draw a triangle spiral
penup()

backward(230)
right(90)                   # Moving to new position for next shape
forward(195)

pendown()
spirallo()                  # Calls spirallo function to draw a octagon spiral
penup()

backward(430)               # Moving to new position for next shape

pendown()
spirallp()                  # Calls spirallp function to draw a pengaon spiral
