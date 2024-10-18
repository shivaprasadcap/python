person= {
    'first_name': 'shiva',
    'second_name': 'prasad',
    'age': 23,
    'city': 'bangalore',
}

print(f"Person name: {person['first_name'].title()} {person['second_name'].title()}\nAge: {person['age']}\nCity: {person['city'].title()}")

favorite_numbers={
    'shiva': 10,
    'dhoni': 7,
    'virat': 18,
    'rohit': 45,
    'ab': 17,
}

print(f"\nShiva: {favorite_numbers['shiva']}\nVirat: {favorite_numbers['virat']}\nDhoni: {favorite_numbers['dhoni']}\nRohit: {favorite_numbers['rohit']}\nAB: {favorite_numbers['ab']}")

#Printing using for loop
print('\nPrinting using for loop:')
for name, fav_num in favorite_numbers.items():
    print(f"{name.title()}: {fav_num}")

#Printing only keys using for loop
print('\nPrinting only keys using for loop:')
for key in favorite_numbers.keys():
    print(key.title())

#Printing only values usinf for loop
print('\nPrinting only values using for loop:')
for value in favorite_numbers.values():
    print(value)

friends= ['virat', 'ab']
for key in favorite_numbers: #Displays same as when you use keys() method
    print(key.title())

    if key in friends:
        print(f"Hi {key.title()}, I see you favorite number is {favorite_numbers[key]}")

for key in sorted(favorite_numbers.keys()):
    print(f"Hi {key.title()}, I know your favorite number is {favorite_numbers[key]}")
