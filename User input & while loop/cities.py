prompt = 'Enter the name of your favorite city: '
prompt += '\nEnter "quit" to stop. '

#No need to use flag as we will be using break to exit loop
# active = True
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f'I would love to visit {city}')