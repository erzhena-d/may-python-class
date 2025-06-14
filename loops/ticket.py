

#create a movie ticketing machine, which always output 
#"sorry your not alowed to pass" if their age is less than 13
# "please call your legal guardian" if age is greater than or equal to 13 and less than 18
# "welcome" if age is greater than or equal to 18 
# in never ending loop

while True:
    age = int(input("Please enter your age: "))
    if age > 0 and age < 13:
        print("Sorry, you're not allowed to pass.")
    elif age >= 13 and age < 18:
        print("Please call your legal guardian.")
    else:
        print("Welcome!")
