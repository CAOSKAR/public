# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'sucuk'],
    'price': 4.99
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza for {pizza['price']}$ "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")