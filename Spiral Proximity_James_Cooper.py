# James Cooper, November 1 2018, Turtle Spiral Proximity Lab
from turtle import *
import random
import math

bgcolor("black") # Set background color to black
hideturtle()
penup()
pencolor("green") # Set border color to green

setx(0)
sety(0)
left(90)
forward(250)

pendown()
right(90)
forward(250)
right(90)
forward(500)
right(90)
forward(500)        # Drawing the border
right(90)
forward(500)
right(90)
forward(320)
left(90)
penup()
backward(250)
pendown()

proximity = (2)

def choice3(): # Defining variable to draw a straight line
    print("Choice3")
    penup()
    speed(0)
    pencolor("red")
    setx(random.randint(-210,210)) # 210
    sety(random.randint(-210,210)) # 210
    print(xcor())
    print(ycor())
    pendown()
    right(random.randint(1,170))
    while not sensor(): # While the line does not hit the border, this code will run
        forward(1)
        if sensor(): # If the function hits a border
            ifsensor() # Calling the ifsensor function

def choice2(): # Defining variable to draw a triangular spiral
    print("Choice2")
    penup()
    speed(0)
    pencolor("orange")
    setx(random.randint(-100,100)) # 100
    sety(random.randint(-100,110)) # 100
    print(xcor())
    print(ycor())
    pendown()
    x = random.randint(10,25)
    for i in range(1,70): # For loop to run 70 times that draws the triangular spiral
        forward(x)
        left(120)
        x = x + 3
        if sensor(): # 
            ifsensor()

def choice1(): # Defining variable to draw a square spiral shape
    print("Choice1")
    penup()
    speed(0)
    pencolor("blue")
    setx(random.randint(-109,109)) # 109
    sety(random.randint(-109,109)) # 109
    print(xcor())
    print(ycor())
    pendown()
    s = random.randint(60,120)
    for i in range(1,31): # For loop to run 31 times that draws the square spiral
        forward(s)
        right(87)
        if sensor(): # If the function hits the border
            ifsensor() # Calling ifsensor function

def choice4(): # Defining variable to draw a pentagon spiral
    print("Choice4")
    penup()
    speed(0)
    pencolor("violet")
    setx(random.randint(-170,170))
    sety(random.randint(-170,170))
    print(xcor())
    print(ycor())
    pendown()
    p = 5
    for i in range(1,31): # For loop to run 31 times that draws the pentagonal spiral
        forward(p)
        right(72)
        p = p + 2
        if sensor(): # If the function hits the border
            ifsensor() # Calling ifsensor function

def sensor(): # Defining variable to proximity sensors
    ymax = 250 # max y-coordinate
    ymin = -250 # minimum y-coordinate
    xmax = 250 # max x-coordinate
    xmin = -250 # minimum x-coordinate
    if ymax-position()[0] < proximity: # Proximity to ymax
        return True
    if xmax-position()[1] < proximity: # Proximity to xmax
        return True
    if position()[1]-ymin < proximity: # Proximity to ymin
        return True
    if position()[0]-xmin < proximity: # Proximity to xmin
        return True
    return False

def spiral(gap = 60): # Defining function to draw a circular spiral
    pencolor("white")
    radius = gap # Assigning variable to another variable 
    while not sensor(): # While loop to draw the spiral as long as it does not hit the sensor
        circum = 2 * math.pi * radius
        fracture = 1/circum
        left(fracture * 360)
        forward(1)
        radius += gap * fracture

def ifsensor(): # Defining function to run general stuff
    while sensor():
        back(30)
        print(xcor())
        print(ycor())
        choice_list = [choice1, choice2, choice3, choice4]# list of choices
        choice_random = random.choice(choice_list) # variable for choosing a random choice from list
        choice_random() # Calling the random choice
        spiral() # Calling spiral function
        ifsensor() # Calling ifsensor functoin

speed(0)
spiral() # Calling spiral function
ifsensor() # Calling ifsensor function
