
# function asks the user to enter a number 
# and prints whether it is positive, negative, or zero.


def check_number(number):
    if number > 0:
        return "The number is positive."
    elif number < 0:
        return "The number is negative."
    else:
        return "The number is zero."
    
number = float(input("Please enter a number: "))
print(check_number(number))