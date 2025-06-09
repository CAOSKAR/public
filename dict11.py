#Store information about a pizza being ordered
pizza = {'crust' : 'thick', 'toppings' : ['mushrooms', 'extra cheese', 'sucuk', 'egg'],}
#Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza" " with the folowing toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")