year=int(input("Enter number of years: "))
units=input("""Enter units: 
1 - for days, 
2 - for weeks, 
3 - for hours
What is your choice?:  
 """)

if units == "1":
    print(f"{year} years is {year * 365} days")
elif units == "2":
    print(f"{year} years is {year * 52} weeks")
elif units == "3":
    print(f"{year} years is {year * 8760} hours")
else:
    print("Invalid choice, please enter 1, 2, or 3.")
# This code takes a number of years as input and converts it to days, weeks, or hours based on the user's choice.