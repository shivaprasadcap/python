prompt = 'Tell me your age. I will display your ticket price: '

while True:
    age = input(prompt)
    age = int(age)

    if age <= 0:
        print('Invalid age. Please provide valid age.') #No break statement as we need user to enter valid age, so continue the loop
    elif age <3:
        print('Free ticket.')
        break
    elif age < 12:
        print('Ticket price is 10 dollars.')
        break
    else:
        print('Ticket price is 12 dollars.')
        break