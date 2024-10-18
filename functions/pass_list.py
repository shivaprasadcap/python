def greet(usernames):
    for user in usernames:
        print(f"Hi {user.title()}, welcome!")

usernames = ['raj', 'ramesh', 'gowtham', 'hrithik']
greet(usernames)

roll_numbers = [1,2,3,4,5,6]

print(roll_numbers)

roll_numbers[0], roll_numbers[-1] = roll_numbers[-1], roll_numbers[0]
print(roll_numbers)