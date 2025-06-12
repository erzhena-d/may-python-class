#create tuples
foods = ("apple", "banana", "orange", "mango", "strawberry", "grape", "mandarin", "strawberry")
calories = (52, 96, 62, 605, 33, 68, 50, 33)

#convert tuples to lists
foods_lists = list (foods)
calories_lists = list (calories)

#print the 5th element(strawberry) and the 2nd last element(grape) with their calories
print(foods_lists[4], calories_lists[4])
print(foods_lists[-2], calories_lists[-2])

#print all unique foods
foods_sets = set(foods)
print(foods_sets)

# Create a dictionary with their unique key, values
foods_dict = {
    "apple": 52,
    "banana": 96,
    "orange": 62,
    "mango": 605,
    "strawberry": 33,
    "grape": 68,
    "mandarin": 50
}
print(foods_dict["mango"])
