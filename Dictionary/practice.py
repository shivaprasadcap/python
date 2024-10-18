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
    if person == person3:
        print(f"{person['first_name'].title()} {person['last_name'].title()}" 
          f" is {person['age']} years old and belongs to {person['city'].title()} city.")
        
for key, value in people[2].items():
    print(f"{key}: {value}")
    