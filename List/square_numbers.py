#Displaying square numbers in a list
squares = []
for number in range(1,10):
    value = number**2
    squares.append(value)

print(squares)

#More simpler program to display sqaures of first 10 digits
squares=[]  #Here the sqaure list becomes empty
for number in range(1,11):
    squares.append(number**2)
print(squares)

# List comprehension
squares=[value**2 for value in range(1,11)]
print(squares)


