# number = 1
# while number <= 5:
#     print(number)
#     number += 1

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue  # The continue statement tells to ignore rest of the loop and continue with loop
    print(number)
