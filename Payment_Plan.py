# James Cooper and Josyiah McCray, September 18 2018, Payment Plan

# Defining function 'asdf' for division
def asdf(x,y):
        return x / y

week = "weekly"
month = "monthly"

# Asking the user information about payment
body = input("What is your name? ")
nameo = input("Now what would you like to purchase? ")
nameo = nameo.lower()
spay = float(input("How much do you need to save for this purchase? "))

# If statement for 'spay' if it is less than or equal to zero
if spay <= 0:

    print("That is an invalid input.")

# Else if statement for 'spay' if it is greater than zero 
elif spay > 0:

# Asking user the frequency of the payment
    meek = input("Would you like to set aside money monthly, or weekly? ") # Asking user to enter 'weekly' or 'monthly' to be user later in the math
    meek = meek.lower()

    if meek == week:

        monday = float(input("How much do you want to set aside for each week? ")) # Asking user to input a value to be set entered at each interval
        if monday <= 0: # If statement for 'monday' if the input from the user is less than or equal to zero
                print("That is an invalid input, please enter a number greater than zero next time.") # Print statement to tell user that entering zero is not valid

        elif monday > 0: # Elif statement for 'monday' if the number they want to set aside for each 'month' or 'week' is greater than zero
            
            print("You will need to put away $", monday, "for", round(asdf(spay,monday),1), "week(s) to reach $", spay, "for your", nameo)# Print statement for how much then need to put away for given amount of time to reach given amount for certain name of purchase
            print("Enjoy your new", nameo, body + "!") # Print statement to tell user to enjoy their purchase giving them their name
            
    elif meek == month: # Elif statement for 'meek' if the input from the user was 'monthly'
        
        # Asking user the frequency of the payment
        tuesday = float(input("How much do you want to set aside for each week or month? ")) # Asking user to input a value to be set entered at each interval
        if tuesday <= 0: # if statement for 'tuesday' if the number they want to set aside for each 'month' or 'week' is less than zero
              print("That is an invalid input, please enter a number greater than zero next time.") # Print statement to tell user that entering zero is not valid

        elif tuesday > 0: # Elif statement for 'tuesday' if the number they want to set aside for each 'month' or 'week' is greater than zero
            print("You will need to put away $", tuesday, "for", round(asdf(spay,tuesday),1), "month(s) to reach $", spay, "for your", nameo) # Print statement for how much then need to put away for given amount of time to reach given amount for certain name of purchase
            print("Enjoy your new", nameo, body + "!") # Print statement to tell user to enjoy their purchase giving them their name
            
    elif meek != week or meek != month: # if variable 'meek' is not a valid input for the two if statement to finish the output

        print("That is an invalid input.") # Print statement telling the user that they did not enter a valid input
        exit() 


