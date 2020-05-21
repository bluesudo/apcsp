# James Cooper, August 27 2018, Conversion Program
from time import sleep # Imports the 'sleep' function from the 'time' module

# Assigning values for euro note variables
fydb = 50 # 50 Euro Variable
twdb = 20 # 20 Euro Variable
tdb = 10 # 10 Euro Variable
fdb = 5 # 5 Euro Variable



usde = int(input("Enter any amount of Dollars to take on your vacation to be converted to Euros: ")) # User enters a integer input for the usde variable which is the dollar amount to be converted to euros
note = usde * .86 # The integer entered in the usde input is now multiplied by 0.86 as that is the current conversion rate of USD to EUROS
print("That is: €", note) # Prints out what the note variable calculated out to be, usd to eur

fyn = int(note // fydb) # Creates variable for the fifty euro note
fyb = note - fyn * fydb # Finds how many fifty euro notes go into 'note' variable
twn = int(fyb // twdb) # Creates variable for the twenty euro note
twb = fyb - twn * twdb # Finds how many twenty euro notes go into 'fyb' variable
tn = int(twb // tdb) # Creates variable for the ten euro note
tb = twb - tn * tdb # Finds how many ten euro notes go into 'twb' variable
fn = int(tb // fdb) # Creates variable for the five euro note
fb = tb - fn * fdb # Finds how many five euro notes go into 'tb' variable
kl = ((note - (fyn * fydb) - (twn * twdb) - (tn * tdb) - (fn * fdb)))
fj = round(kl,3
           )

# Prints out each amount of euro notes
print(fyn, "50 Euro Notes")
print(twn, "20 Euro Notes")
print(tn, "10 Euro Notes")
print(fn, "5 Euro Notes")
print(fj, "Euros Left Over")
sleep(5)
