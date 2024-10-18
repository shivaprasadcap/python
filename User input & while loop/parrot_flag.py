# what if you have multiple conditions to check other than 'quit'
prompt = 'Tell me something, I will repeat it back to you:'
prompt += '\nType "quit" to exit. '

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)