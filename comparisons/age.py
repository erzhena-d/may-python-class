age=int(input("Enter age: "))

if age < 13 and age > 0: 
    print(f"{age} years is a child")
elif age >= 13 and age < 18:
    print(f"{age} years is a teenager")
elif age >= 18 and age < 65:
    print(f"{age} years is an adult")
elif age >= 65:
    print(f"{age} years is an elder")
else:
    print("Invalid input.")
# This code takes an age as input and categorizes it into child, teenager, adult, or elder based on the age range.