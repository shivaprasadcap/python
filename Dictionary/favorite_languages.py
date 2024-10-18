favorite_languages={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for key in favorite_languages.keys():
    print(key.title())

print()
for key in favorite_languages:
    print(key.title())

print()
for value in favorite_languages.values():
    print(value)

print()
for key, value in favorite_languages.items():
    print(f"{key.title()} likes {value} language.")

#Printing only unique languages in the favorite_languages.values()
print()
for value in set(favorite_languages.values()):
    print(value)

#You can create a set using {flower} brackets
print()
languages= {'python', 'rust', 'c', 'python', 'java', 'c'}
print(languages)

print()
names=['jen', 'raj', 'tom', 'sarah', 'phil', 'sam']
for name in names:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for mentioning your favorite language.")
    else:
        print(f"{name.title()}, please mention your favorite language.")