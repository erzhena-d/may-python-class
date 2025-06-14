#code shows the fibonacchi sequence and stoprs at the limit


limit = int(input("Enter a limit: "))
first = 0
second = 1
print(first)
print(second)

next = first + second

while next < limit:
    print(next)
    first = second
    second = next
    next = first + second

