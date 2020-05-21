# James Cooper, October 19 2018, Magic 8 Ball
import random # Imports random module

# Create list of strings for the respose to the 8 ball question
list_response = ['Concentrate and ask again!', 'You may rely on it.', ' Without a doubt.', 'My reply is no.', 'Why would you want that?', 'I am certian.', 'Outlook not so good.', 'As I see it yes.', "Better if you didn't ask.", "You're not ready to hear that."]
# Create list of strings for the question of being asked to the user
list_questions = ["Okay, what is your question for me? ", "Awesome, what is the question? ", "Please, tell me your question? ", "Your question has been requested. "]
# Create list of strings for the question of being asked if user wants to ask another question
list_anquestion = ["How about another question for me? ", " Would you like to ask another question? ", "Another one? ", "Have time for one more question? ", "Please ask another question, I insist? "]
name = input('What is your name? ') # # User input for their name

sa = "Hi %s I'm 8 ball, do you have a question for me? " % name # Assigning variable 'sa' to a string of characters

ball_intro = input(sa) # User input asking the 'sa' variable
ball_intro.lower() # Setting the input from 'ball_intro' to lowercase
print('') # Print blank line

while ball_intro == "yes": # While loop for 'ball_intro' is equal to "yes"
    
    answer1 = random.choice(list_response) # Variable with random string from 'list_response'
    qrandom = random.choice(list_questions) # Variable with random string from 'list_questions'
    arandom = random.choice(list_anquestion) # Variable with random string from 'list_anquestion'
    ball_question = input(qrandom) # User input with 'qrandom' as the output
    print(answer1) # Print the 'answer1' variable
    print('') # Print blank line
    ball_swift = input(arandom) # User input with 'arandom' as the output
    ball_swift.lower() # Setting the input from 'ball_swift' to lowercase

    if ball_swift == "yes": # if statement if 'ball_swift' is "yes"
        ball_intro == "yes" # Runs back to the while loop statement
        
    if ball_swift == "no": # If statement if 'ball_swift' is "no"
        print('') # Print blank line
        print("That's okay, you can ask me anything another time! ") # Print statement telling the user that they can use the program again
        
if ball_intro == "no": # If statement if 'ball_intro' is "no"
    print("Why did you open me?") # Print statement telling user that the program will quit in a sarcastic way
    exit() # Exits program
