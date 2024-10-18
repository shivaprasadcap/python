person1 = {
    'first_name': 'shiva',
    'last_name': 'prasad',
    'age': 23,
    'city': 'bangalore',
}

person2 = {
    'first_name': 'virat',
    'last_name': 'kohli',
    'age': 34,
    'city': 'delhi',
}

person3 = {
    'first_name': 'rohit',
    'last_name': 'sharma',
    'age': 35,
    'city': 'mumbai',
}

people = [person1, person2, person3] #Don't use quotation marks as it will consider the elements as string literals.

for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()}" 
          f" is {person['age']} years old and belongs to {person['city'].title()} city.")

print()
pet1 = {
    'name': 'tommy',
    'animal_type': 'cat',
    'owner': 'rohit',
}

pet2 = {
    'name': 'jimmy',
    'animal_type': 'dog',
    'owner': 'kohli',
}

pets = [pet1, pet2]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['animal_type']} and is owned by {pet['owner'].title()}.")

print()
favorite_places = {
    'paris': 'virat',
    'london': 'root',
    'new york': 'shiva',
}

for key, value in favorite_places.items():
    print(f"{value.title()}'s favorite place is {key.title()}")

favorite_numbers = {
    'virat': [18],
    'shiva': [23, 34],
    'rohit': [45],
    'dhoni': [7, 22, 27],
}

#this is wrong, won't display numbers properly
# for name in favorite_numbers:
#     print(f"{name.title()}'s favorite number(s): ")
#     for number in favorite_numbers.values():
#         print(f"\t{number}")

print()
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite number(s): ")
    for number in numbers:
        print(f"{number}")

cities = {
    'bangalore': {
        'country': 'india',
        'population': '13 million',
        'fact': 'capital city of Karnataka'
    },

    'london': {
        'country': 'england',
        'population': '8.8 million',
        'fact': 'capital city of England'
    },

    'washington DC': {
        'country': 'USA',
        'population': '5.4 million',
        'fact': 'capital city of USA'
    },
}

for city, city_info in cities.items():
    print(f"{city.title()}:")
    print(f"\tCountry: {city_info['country'].title()}\n\tPopulation: {city_info['population']}\n\tFact: {city_info['fact']}")

cities['delhi'] = {
    'country': 'india',
    'population': '20 million',
    'fact': 'capital city of India'    
}

for city, city_info in cities.items():
    print(f"{city.title()}:")
    print(f"\tCountry: {city_info['country'].title()}\n\tPopulation: {city_info['population']}\n\tFact: {city_info['fact']}")