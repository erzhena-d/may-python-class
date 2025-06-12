
discount=0
sales_tax=0.1

def tax_func(price):
    """Calculate the sales tax for a given price."""
    return price * sales_tax

def discount_func(price, discount):
    discount_sum = price * (discount / 100)
    """Calculate the discount for a given price."""
    return discount_sum


price = float(input("Enter the price of the item: "))


tax = tax_func(price)

if price < 0:
    print("Price cannot be negative.")
if price > 100 and price <= 200:
    discount = discount_func(price, 10)
elif price > 200:
    discount = discount_func(price, 20)

total_price = price + tax - discount
print(total_price)