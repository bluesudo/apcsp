# James Cooper, 15 November 2018, Pool Table Turtle Lab

from turtle import *

s = Turtle() # 
t = Turtle() # global turtle variables
f = Turtle() #
tex = Turtle()#

title("Pool Table") # Title of program in top bar 
bgcolor("black") # Set background color to black

speed(0) # Set turtle speed to maximum speed

t.ht() # 
f.ht() # 
tex.ht() # global hiding of turtles in the wild, the predators have come out
s.ht() # 

def bounce_horizontal(): # Defining fucntion that sets the ball parameters and sends it horizontally
    
    t.color("white")  #section to draw ball
    t.pu() # Pen up for turtle so a line is not drawn
    t.shape("circle") # Draws a circle
    t.shapesize(2,2) # Set shape parameters
    t.setpos(0,0) # Sets position
    t.st() # Shows the turtle
    delay(25) # Delay of movement when working with whole program
    t.goto(282,0) # Moves ball from start position to new position - causes movement

def tableout(): # Defining a function that will draw the table and my name

    f.color("#84391b") # Set color of shape to brown
    f.pu() # Pen up for turtle so a line is not drawn
    f.shape("square") # Draws a square
    f.fillcolor("#84391b") # Set color of shape filling to brown
    f.shapesize(20,32,25) # Set shape parameters
    f.setpos(0,0) # Set turtle position to the origin
    f.st() # Shows the turtle
    
    s.color("green") # Set color of shape to green
    s.pu() # Pen up for turtle so a line is not drawn
    s.shape("square") # Draws a square
    s.fillcolor("green") # Set color of shape filling to green
    s.shapesize(17,29,25) # Set shape parameters
    s.setpos(0,0) # Set turtle positoin to the origin
    s.st() # Shows the turtle

    tex.color("white") # Setting turtle color to white
    tex.pu() # Pen up for turtle so a line is not drawn
    tex.setpos(590,-400) # Setting turtle coordinates
    tex.write("- James Cooper",align = "left",font = ("Ariel",20,"normal")) # Writing my name
    
def bounce_diag(): # Defining a function that will 
    
    t.st() # Shows the turtle
    delay(30) # Sets delay of movement
    t.goto(0,162) # Tells turtle to move to a point
    
def bounce_vert(): # Defining a function that will move the ball vertically to a point

    t.st # Shows the turtle
    delay(35) # Sets delay of movement
    t.goto(0,-72) # Tells turtle to move to a point
    
def main(): # Defing variable for a single calling function
    tableout() # 
    bounce_horizontal()# Calling of fucntions in order of movement and purpose
    bounce_diag() # 
    bounce_vert() # 
    
main() # Calling the main function
