number = input('Enter a number and I will tell you whether it is an odd or even number: ')
number = int(number)

if number % 2 == 0:
    print(f"\n{number} is even.")
else:
    print(f"\n{number} is odd.")