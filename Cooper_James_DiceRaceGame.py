# James Cooper, October 15 2018, Dice Race Game
import random # Import random module
import time # Import time module

alt = 0 # Initiating alt to the value of 0
x = 1 # Initiating x to the value of 1

ps1 = [] # Creation of list for Player 1 scores for each time the whole loop runs
ps2 = [] # Creation of list for Player 2 scores for each time the whole loop runs

while x <= 6: # While loop for while x is less than or equal to 6
    alt = (alt + 1) % 2 # Function whos result will alternate between 1 and 0 everytime the loop is ran
    x = x + 1 # Adds 1 to x everytime the loop runs
    if alt == 1: # If statement if variable 'alt' is equal to 0
        num1 = random.randint(1,6) # Variable for random number from 1 to 6
        print("Player 1") # Prints statement for who is rolling
        print("The die rolled to", num1) # Print statement for the random integer of 'num1'
        ps1.append(num1) # Adds integer to 'ps1' list
        ps1f = sum(ps1) # Assigning variable to sum of all values in 'ps1' list
        print(ps1f, "is your new score") # Print statement for the current sum of 'ps1' list
        print("") # Print blank line for spacing
        time.sleep(2)
    if alt == 0: # If statement if variable 'alt' is equal to 0
        num2 = random.randint(1,6) # Variable for random number from 1 to 6
        print("Player 2") # Print statement for who is rolling
        print("The die rolled to", num2) # Print statement for the random integer of 'num2'
        ps2.append(num2) # Adds integer to 'ps2' list
        ps2f = sum(ps2) # Assigning variable to sum of all values in 'ps2' list
        print(ps2f, "is your new score") # Print statement for the current sum of 'ps2' list
        print("") # Print blank line for spacing
        time.sleep(2)

s1 = sum(ps1) # Assigning variable to the sum of all values in 'ps1' list
s2 = sum(ps2) # Assigning variable to the sum of all values in 'ps2' list

if s1 > s2: # If statement if variable 's1' is greater than 's2'
    print("Player 1 won the game!", '\n') # If statement if variable 's1' is greater than 's2'
if s1 < s2: # If statement for if variable 's1' is less than 's2'
    print("Player 2 won the game!",'\n') # Print statement if variabele 's1' is less than 's2'
if s1 == s2: # If statement for if variable 's1' and 's2' are equal
    print("The game was a tie!", '\n') # Print statement if variable 's1' and 's2' are equal

print("Player 1 final score:", s1) # Print statement of player 1's final score 
print("Player 2 final score:", s2) # Print statement of player 2's final score
