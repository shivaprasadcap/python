# message = input('Tell me something, I will repeat it back to you: ')
# print(message)

prompt = 'Tell me something, I will repeat it back to you: '
prompt += "\nEnter 'quit' to stop."

message = ''
# this prints "quit" when "quit" is given as output
# while message != 'quit':
#     message = input(prompt)
#     print(message) 

while message != 'quit':
    message = input(prompt)
    if message != 'quit':    #Doesn't display 'quit'
        print(message) 


