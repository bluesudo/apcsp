# James Cooper, September 6 2018, OwnFunction
import math # Imports Math Module for the math.sqrt() function
# This will solve the pythagorean theorem asking for side a and side b then finding side c for you(the hypotenuse)

def daj(x,y): # Defines the 'daj' function with variables 'x' and 'y'
    return math.sqrt(x**2 + y**2) # What the 'daj' function will perform with the two variables, squaring each and adding the two together then finding the square root of the number

p1 = float(input("Enter side A: ")) # User enters first number to be entered into 'daj' function as the 'x' variable
p2 = float(input("Enter side B: ")) # User enters second number to be entered into the 'daj' function as the 'y' variable

std = daj(p1,p2) # Giving the math a variable to look better in the print statement below in the form of 'std'

print("Side C is: ", round(std,3)) # Prints out the result of 'daj' function and rounds the number to three decimal places
