list=[value for value in range(1,1000001)]
# print(list)
print(max(list))
print(min(list))
print(sum(list))

#Cube of numbers
list=[value**3 for value in range(1,11)]
for cube in list:
    print(cube)

cube_numbers=[]
for value in range(1,11):
    cube=value**3
    cube_numbers.append(cube)
print(cube_numbers)