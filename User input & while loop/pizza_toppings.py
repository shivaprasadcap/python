# Initialize an empty list to store pizza toppings.
toppings = []

# Set up the prompt for user input.
prompt = 'Tell me the toppings you want on your Pizza: '
prompt += '\nType "quit" if you\'ve finished adding toppings. '

# Flag to control the loop.
active = True

# Start a loop to collect toppings from the user.
while active:
    # Get user input.
    message = input(prompt)

    # Check if the user wants to quit.
    if message == 'quit':
        active = False
    else:
        # Add the topping to the list.
        toppings.append(message)
        # Provide feedback to the user.
        print(f'\nYou have added "{message.title()}" as your topping.\n')

# End of the loop. User has finished adding toppings.

# Display all the selected toppings.
print('\nAll your toppings:')
for topping in toppings:
    print(topping.title())
