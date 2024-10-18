#List in dictionary
favorite_languages = {
    'jen': ['python', 'rust'],
    'edward': ['c'],
    'sarah': ['go', 'rust'],
    'phil': ['python', 'haskell'],
}

#Displaying only keys
for key in favorite_languages.keys():
    print(key)
print()
for key in favorite_languages:
    print(key)

print()
#Displaying only values
for value in favorite_languages.values():
    print(value)
print('chacha')

#Printing values of individual keys
for value in favorite_languages['edward']:
    print(value)

#Printing individual values of a particular key using list comprehension
print('Jen:')
[print(value) for value in favorite_languages['jen']]
print('Edward:')
[print(value) for value in favorite_languages['edward']]
print('Phil:')
[print(value) for value in favorite_languages['phil']]
print('Sarah:')
[print(value) for value in favorite_languages['sarah']]

#Using simple for loop
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language(s):")
    for language in languages:
        print(f"\t{language.title()}")