# James Cooper, October 1 2018, For and While Loop Codes



 # 1

apache2 = [] # Creating a empty list to store the 'names' of people for later

user = int(input("How many people do you want to invite to the party? ")) # Asking user to enter how many people they would like to invite to the party with in integer.

if user > 10: # If statement for if the amount entered into 'user' is greater than 10
    print("Too many people.") # Print statement telling user that they entered a value too big

elif user > 0: # If statement for if the amount entered into 'user' is greater than 0, it's not a party if there are only 0 people

    for i in range(0,user): # For loop for running code for integers from 0 to the value entered into 'user'
        name = input("Name(s): ") # Asking user to enter string of characters for a name for the guests being invited to the party
        print(name, "has been invited.") # Print statement telling the user that 'name' input has been invited
        apache2.append(name) # Appending the input from 'name' to the list of 'apache2'


    print("The list of invited people is", apache2) # Print statement for printing out the 'apache2' list

elif user <= 0: # Elif statement if the value entered into 'user' is less than or equal to 0
    print("Not enough people, can't have a party with no people") #Print statement telling the user that it's not a party with less than or just 0 people
    
 # 2

monkey = 6 # Assigning the value of 6 to 'monkey' as the amount of monkeys starts at 6

while monkey <= 6: # While loop for the value of 'monkey' being less than or equal to 6

    print("There are", monkey, "monkeys jumping on the bed. If one falls off and bumps his head,",'\n', "how many monkeys are jumping on the bed?") # Print statement for stating the value of 'monkey'
    asdf = int(input("Monkeys Remaining? ")) # Asking for user input for what the value of 'monkey' is
    monkey = monkey - 1 # Subtractig 1 from 'monkey' as a monkey has fallen off the bed
    
    if asdf == monkey: # if statement if the 'asdf' input from the user is the correct value of 'monkey' after 1 is subtracted from it
        print("Good!") # Print statement telling the user that they are correct or 'good'
        
    else: # Else statement if the user does not enter the correct value for 'asdf'
        print("Try Again!") # Print statement telling the user that the value entered was incorrect
        monkey = monkey + 1 # Adding 1 to 'monkey' otherwise it would have been subtracted 1 again resulting in losing monkeys without entering how many are left
        
    if monkey == 0: # If statement for if the value of 'monkey' is 0
        print("There are no more monkeys jumping on the bead as they have all bumped their head!") # Print statement telling the user that all of monkeys have fallen off of the bed, or the value of 'monkey' is 0
        break # Breaking the while loop as the value of 'monkey' is 0

