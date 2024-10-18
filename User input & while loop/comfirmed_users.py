# unconfirmed_users = ['alice', 'john', 'brian']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f'Verifying user: {current_user.title()}')
#     confirmed_users.append(current_user)

# print('\nConfirmed users:')
# for user in confirmed_users:
#     print(user.title())

unconfirmed_users = ['alice', 'john', 'brian']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop(0)  # Remove the user from the beginning of the list

    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

print('\nConfirmed users:')
for user in confirmed_users:
    print(user.title())
