# function takes a user's name as input and prints a greeting message. 
# if the name is "Alice" or "Bob", the program should print "Hello, Alice/Bob!" 
# otherwise, it should print "Hello, guest!".

def greet_user():
    name = input("Please enter your name: ")
    if name == "Alice" or name == "Bob":
        return f"Hello, {name}!"
    else:
        return "Hello, guest!"

print(greet_user())
