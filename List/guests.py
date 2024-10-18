guests =['Sachin', 'Virat', 'Dhoni']
for guest in guests:
    print(f'Hello {guest}, welcome to my Party!')

print('\nVirat is unable to join the Party')
guests[1]= 'Raina'
for guest in guests:
    print(f'Hello {guest}, welcome to my Party!')

print('\nWe have more guests!')
guests.insert(0, 'Rohit')
guests.insert(2, 'Zaheer')
guests.append('Ashwin')
for guest in guests:
    print(f'Hello {guest}, welcome to my Party!')

print('\nOh no! We have only 2 seats available.')
guests.pop()
guests.pop()
guests.pop()
guests.pop()
for guest in guests:
    print(f'Hi {guest}, welcome to my Party!')

del guests[0]
del guests[0]
print(f'\nMy list is empty now: {guests}')