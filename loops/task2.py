# while loop asking the user to input an integer till the sum of those values reaches 100 or above
# don't forget to store all those values and print the condition was met (Use a list to store all the values)

sum = 0
total = []

while sum < 100:
    num = int(input("Please enter an integer: "))
    total.append(num)
    sum += num
print("The total is now", total)