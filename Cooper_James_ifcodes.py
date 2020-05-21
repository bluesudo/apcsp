# James Cooper, September 11 2018, If Codes

# If-Else 1
print("Problem 1")

n1 = int(input("Enter a number that is under 30: ")) # Asks user for input under a value of 30
if n1 < 30:
    print("Thank You!") # Print message if the input is under 30
else:
    print("Too High") # Print message if the input is anything over 30

# If-Else 2
print("")
print("Problem 2")

color = input("Enter your favorite color: ") # Asks user to enter their favorite color
color = color.lower()
if color == "blue":
    print("I like blue too!") # Print message if the string of characters entered is the color blue
elif color != "blue":
    print("I don't like that color, I prefer blue") # Print message if the string of characters entered is not the color blue

# If-Else 3
print("")
print("Problem 3")

age = int(input("Enter your age as an integer: ")) # Asks the user to input their age as a integer
if age >= 18:
    print("You can vote") # Print message if the input is greater than or equal to 18
elif age == 16:
    print("You can learn to drive") # Print message if the input is 16
elif age == 17:
    print("You can learn to drive") # Print message if the input is 17
elif age <= 15:
    print("You can go Trick-or-Treating") # Print message if the input is less than or equal to 15

# If-Elif 4
print("")
print("Problem 4")

eula = int(input("Enter a 1, 2 or 3: ")) # Asks user to input a 1, 2, or 3
if eula == 1:
    print("Thank you") # Print message if the input from user is 1
elif eula == 2:
    print("Awesome") # Print message if the input from the user is 2
elif eula == 3:
    print("Love the 3!") # Print message if the input from the user is a 3
else:
    print("ERROR!") # Print message if the input is not 1, 2, or 3

# Bonus If-Elif-Else
print("")
print("Problem Bonus")

from time import sleep # Import sleep function from time module for later use

dash = input("Would you like to hear a did you know fact? ") # Input asking for user input whether or not they would like to hear a did you know fact
dash = dash.lower()
if dash == "yes": # If statement if input is yes
    print("Did you know a bear has 42 teeth!") # First did you know fact
    jkl = input("Want to hear another one? ") # Asking user to read another did you know fact
    jkl = jkl.lower()
    if jkl == "yes":
        sleep(2)
        print("A lemon contains more sugar than strawberries") # Second did you now fact
    elif jkl == "no":
        print("Okay.") # Print message if the input for jkl is 'no' 
        sleep(3)
        exit() # Exit program as no more services are requested
    elif jkl != "yes" or jkl != "no":
        print("Okay.") # Print message if the input for 'jkl' is not a correct input
        sleep(3)
        exit() # Exit program as user failed to enter a correct input
elif dash == "no":
    print("How about a joke instead.")
    asdf = input("Ready?") # Asks user if they are ready to hear a joke
    asdf = asdf.lower()
    if asdf == "yes":
        print("Why did I throw the clock out of the window?") # Print message of the joke if the response to 'asdf' is 'yes'
        sleep(2)
        print("Because I wanted to see time fly!") # Print message of the other half of the joke
    elif asdf == "no":
        print("Okay.") # Print message if question to hear a joke is 'no'
        sleep(3)
        exit() # Exit program as user said no to any more messages
    elif  asdf != "yes" or asdf != "no":
        print("Okay.") # Print message if the input from the user is not a valid input
        sleep(3)
        exit() # Exit program as user failed to enter a valid input
elif dash != "no" or dash != "yes":
    print("Okay.") # Print message if the input from the user is not a valid input
    sleep(3)
    exit() # Exit program as user failed to enter a valid input
