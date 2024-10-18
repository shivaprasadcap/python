#Dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for key, value in users.items():
    print(key)
    print(value)
print()

# for username, user_info in users.items():
#     for key2 in user_info:
#         print(key2['first'])

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    print(f"\tFullname: {user_info['first'].title()} {user_info['last'].title()}") #user_info is like an array, call which u need using index. No need to use another for loop.
    print(f"\tLocation: {user_info['location'].title()}")