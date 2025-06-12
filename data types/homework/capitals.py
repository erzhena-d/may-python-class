#create a dictionary, where the keys are country names and the values are their capitals
country_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "UK": "London",
}

#prompt the user to enter a country name and print its capital
country = input("Enter a country name: ")
print(f"The capital of {country} is {country_capitals.get(country, 'not found')}.")




#country_capital.get() is used to retrive the value associated with the key (country name) from the dictionary
#if the country is not found - it returns 'not found'
#in parentheses, we use arguments of the the first argument is country name - which is user input, 
#and the second argument is the default value 'not found' if the key does not exist in the dictionary.

#dictionary.get(key, default) 