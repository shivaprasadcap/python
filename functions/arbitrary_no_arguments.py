def make_pizza(size, *toppings):
    
    print(f"Please make me a {size}-inch Pizze with below toppings: ")
    for topping in toppings:
        print(topping)


make_pizza(12, 'tomato')
print()
make_pizza(16, 'tomato', 'corn', 'paneer', 'extra-cheese')