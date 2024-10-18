# List inside a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['extra cheese', 'mushrooms']
}

print(f"You ordered a {pizza['crust']}-crust Pizza "
      "with following toppings:")

for topping in pizza['toppings']: #You can individually call list items like this
    print(f"\t{topping}")

for value in pizza:
    print(value)