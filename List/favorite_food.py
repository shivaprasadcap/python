#Copying a list
my_food=['Burger', 'Biryani', 'Paneer', 'Butter Chicken']
friends_fav=my_food[:] #Type like this when copying list to avoid errors, here you are creating a new list 'friends_fav' and assigning values to the list from 'my_food' list.
print(f'My favourite foods: {my_food}')
print(f"My friend's favourite foods: {friends_fav}")

my_food=['Burger', 'Biryani', 'Paneer', 'Butter Chicken']
print(f'\nMy favourite foods: {my_food}')
friends_fav=my_food #Don't use this method, here the same list has 2 labels i.e, friends_fav and my_food.
friends_fav.append('Pizza')
my_food.append('Vada')
print(f'My favourite foods: {my_food}')
print(f"My friend's favourite foods: {friends_fav}")

# Correct method
my_food=['Burger', 'Biryani', 'Paneer', 'Butter Chicken']
print(f'\nMy favourite foods: {my_food}')
friends_fav=my_food[:] #Correct method
friends_fav.append('Pizza')
my_food.append('Vada')
print(f'My favourite foods: {my_food}')
print(f"My friend's favourite foods: {friends_fav}")

#For loop in list
print('\nMy favourite foods:')
for food in my_food:
    print(food)
print("My friend's favourite foods:")
for food in friends_fav:
    print(food)