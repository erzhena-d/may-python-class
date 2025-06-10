foods=["burger", "pizza", "taco"]
drinks=["coke", "pepsi", "milk"]

print(len(drinks))
print(f"Can I get {foods[2]} and {drinks[-1]}")

print(foods[0])
print(drinks[-1])

foods.append("salad")
print(foods)

print(foods.count("salad"))

foods.extend(["cheeseburger", "sushi"])
print(foods)