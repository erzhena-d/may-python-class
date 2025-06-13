tip=int(input("Input tips amount: "))

if tip == 15:
    print(f"{tip}% is a standart amount of tip")
elif tip > 15 and tip < 18:
    print(f"{tip}% is a good amount of tip")
elif tip >= 18 and tip < 20:
    print(f"{tip}% is a great amount of tip")
elif tip >= 20:
    print(f"{tip}% is making you my day")
else:
    print("Invalid input, please enter a valid tip amount.")
# This code takes a tip amount as input and categorizes it into standard, good, great, or exceptional based on the tip percentage.
