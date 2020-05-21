# James Cooper, December 11 2018, Lab: Prize or Perish

import random # Import random module to select random choices and integers
import time # Import time module to create time delays

name = input("What is your name? ")
print("Hello", name + "!",  "Welcome to a game called Prize or Perish! ")               # Introducing the player to the game
print("You will enter a cave to start your adventure!")
print('')

# These are lists that contain the responses the game gives you based on your cave choice
cave_good_list = ["You enter the cave and you can see a light at the end, there are no obstacles.", "You approach the cave to find a guardian at the entrance of the cave, \n and he guides you through to safety.", "You enter the cave and you fight off the cyclops defending the exit."]
cave_bad_list = ["You enter the cave to slip and fall into and endless pit, you never return.", "You lose your sword and get attacked by a wild sasquatch.", "You get lost deep into the cave a fall into insanity."]
cave_badrgood = ["good", "bad"]

def player_win(): # Creating a function if the player chose to enter a good cave
    time.sleep(2)
    print("Congragulations! You made it though the cave and survived!")
    
def player_death(): # Creating a function if the player chose to enter a bad cave
    time.sleep(2)
    print("Sorry, you did not make it through the cave and died!")

def cave_choice(): # This function will ask the player what cave they wish to enter
    caveinput = "Which cave would you like to enter %s, 1 or 2? " % name
    cave = float(input(caveinput))
    print('')
    
    while cave == 1 or cave == 2: # While loop for when the player chooses to enter cave 1 or cave 2
        caves = random.choice(cave_badrgood) # Randomizing the cave selection of being a good cave or a bad cave
        print("Analyzing the cave...")
        print('')
        time.sleep(2)
        print("You chose to enter a",caves, "cave.")
        print('')
        
        if caves == "good": # If statement for if the player enters a good cave
            time.sleep(2)
            print(random.choice(cave_good_list)) # Selecting a random option of responses from the cave_good_list
            print('')
            player_win() # Calls the player_win function as they entered a good cave
            print('')
            play_again() # Calls the play_again function to see if they want to play agian
            
        if caves == "bad": # If statement for if the player enters a bad cave
            time.sleep(2)
            print(random.choice(cave_bad_list)) # Selecting a random option of responses from the cave_bad_list
            print('')
            player_death() # Calls the player_death function as the player entered a bad cave
            print('')
            play_again() # Calls the play_again function to see if the player wants to play again

    if cave != 1 and cave != 2:
        print("That is not a valid cave choice. Please enter 1 or 2 ")
        cave_choice()

def play_again(): # Function that asks the player if they want to play again
    playagain = input("Would you like to play again? ")
    playagain.lower() # Converting the player input of whether or not they want to play again to lowercase
    
    if playagain == "yes": # If statement for if the player enters yes to wanting to play again
        cave_choice() # cave_choice function is called to play

    if playagain == "no": # If statement for if the player enters no to wanting to play again
        print('')
        print("Closing the program in 3 seconds... ")
        time.sleep(3)
        exit() # This closes the program
        
    else: # Else statement for if the player does not enter yes or no
        print("That is not a valid input, please enter yes or no. ")
        play_again() # Calls the play_agian function as the player will have the option of entering a valid input

cave_choice() # Calling the cave_choice function to start the program

        

