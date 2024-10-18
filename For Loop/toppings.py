required_toppings = ['extra cheese', 'mushroom', 'extra pepper']
for toppings in required_toppings:
    if toppings == 'extra pepper':
        print(f'{toppings.title()} is not available.')
    else:
        print(f'{toppings.title()} has been added.')
print('\nFinished making your Pizza!')