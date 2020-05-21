# James Cooper Ayden Voge, October 9 2018, Guess the Number Partner Lab
#random number is chosen between 1 and 25 and defining variables 
import random
guess = 0
uname = input("What is your name? ")
rnum = random.randint(1,25)

print(uname, ", I'm thinking of a number between 1 and 25")
#player gets 6 guesses 
while guess <= 6:
    asdf = int(input("Guess what number I am thinking of. "))
    guess = guess + 1
#varable for guesses is added to everytime it loops
    if asdf == rnum:
        print("Congragulations", uname, "it took you", guess, "guesses and the number was", rnum)
        break
#if player guesses the number then the loop breaks
    elif asdf < rnum:
        print("Too low of a guess!")
#if the guess is less than the random number then it will indicate so
    elif asdf > rnum:
        print("Too high of a guess!")
#if the guess is less than the random number then it will indicate so
if guess == 7:
    print("You lost", uname, "but the correct number was", rnum)
#if player exceeds 6 guesses then the game is over 
