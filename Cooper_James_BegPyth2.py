# James Cooper, August 22 2018, BegPyth2
from time import sleep
def add(a,s):
    return a + s

def asd(a,s,d):
    return (a + s) / d

def div(a,s):
    return a / s

def hour(a):
    return a * 24

def min(a):
    return a * 1440

def sec(a):
    return a * 86400

print("Enter two numbers, I will add them together.")
n1 = float(input("First number: "))
n2 = float(input("Second number: "))
print("The total is:", add(n1,n2))
sleep(1)
print("Enter three numbers, I will add the first two together then divide that result by the third number.")
n3 = float(input("First number: "))
n4 = float(input("Second number: "))
n5 = float(input("Third number: "))
print("The answer is", asd(n3,n4,n5))
sleep(1)
print("Enter the total price of your meals bill and I will divide it by the total number of diners.")
n11 = float(input("Total price: "))
n12 = float(input("Total diners: "))
print("Each person has to pay:", "$", div(n11,n12))
sleep(1)
print("Enter any amount of days, I will tell you how many hours, minutes, or seconds are in that amount of days.")
d = float(input("Amount of days: "))
print("In", d, "days, there are:", hour(d), "hours", "or", min(d), "minutes", "or", sec(d), "seconds")
sleep(3)
