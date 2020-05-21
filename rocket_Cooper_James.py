# James Cooper, 15 November 2018, Rocket Flying in the Sky Turtle Lab

from turtle import *

bgcolor("#2c7af7") # Set background color to blue
title("Rocketship") # Set window title to "Rocketship"

gr = Turtle() #
sun = Turtle() #
abo = Turtle() #
ato = Turtle() #    Global creation of turtles
atr1 = Turtle() #
atr2 = Turtle() #
atr3 = Turtle() #

gr.penup() #
sun.penup() #
abo.penup() #
ato.penup() # Global penups of turtles
atr1.penup() #
atr2.penup() #
atr3.penup() #

def ground(): # Defining function to draw the ground
    sun.ht() #
    sun.pencolor("#2c7af7") #
    sun.goto(400,265) #
    sun.st() #
    sun.color("black") #    This turtle draws the cirlce that represents the sun
    sun.shape("circle") #
    sun.shapesize(5,5) #
    sun.fillcolor("yellow") #
    
    gr.ht() #
    gr.pencolor("#2c7af7") #
    gr.sety(-500) #
    gr.st() #   This turtle draws the rectangle that represents the ground
    gr.color("#1aaf0f") #
    gr.shape("square") #
    gr.shapesize(20,250) #

def rockettrail(): # Defining function that draws the rocket trails
    atr1.ht() #
    atr1.pencolor("#2c7af7") #
    atr1.sety(-375) #
    atr1.st() #
    atr1.color("black") #   This turlte is the largest triangle for the rocket trail
    atr1.left(270) #
    atr1.shape("triangle") #
    atr1.shapesize(2,6) #
    atr1.fillcolor("yellow") #

    atr2.ht() #
    atr2.pencolor("#2c7af7") #
    atr2.sety(-365) #
    atr2.st() #
    atr2.color("black") #   This turlte is the second largest triangle for the rocket trail
    atr2.left(270) #
    atr2.shape("triangle") #
    atr2.shapesize(2,4) #
    atr2.fillcolor("orange") #

    atr3.ht() #
    atr3.pencolor("#2c7af7") #
    atr3.sety(-355) #
    atr3.st() #
    atr3.color("black") #   This turtle is the smallest triangle for the rocket trail
    atr3.left(270) #
    atr3.shape("triangle") #
    atr3.shapesize(2,2) #
    atr3.fillcolor("red") #

def rocketbody(): # Defining function that draws the rockets body
    ato.ht() #
    ato.pencolor("#2c7af7") #
    ato.sety(-210) #
    ato.st() #
    ato.color("black") #    This turtle draws the top triangle of the rocket
    ato.left(90) #
    ato.shape("triangle") #
    ato.shapesize(2,3) #
    ato.fillcolor("red") #
    
    abo.ht() #
    abo.pencolor("#2c7af7") #
    abo.sety(-280) #
    abo.st() #
    abo.color("black") #    This turtle draws the body rectangle of the rocket
    abo.shape("square") #
    abo.shapesize(6,2) #
    abo.fillcolor("white") #
    
    rockettrail() # Calling of the rockettrail() function

def rocketmove(): # Defining function that moves the rocket and trail upwards
    x = -205
    for i in range(0,1000): # Loop to move the rocket and trails
        x = x + 4
        ato.sety(x+50)
        abo.sety(x-25)
        atr1.sety(x-115)
        atr2.sety(x-105)
        atr3.sety(x-95)

def main(): # Defining function that is a main function that calls all other functions
    ground() #
    rocketbody() #  Calling of all function under one function
    rocketmove() #

main()
