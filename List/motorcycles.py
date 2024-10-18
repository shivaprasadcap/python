motorcycles=['Honda', 'Hyundai', 'Ferrari', 'Tata']
print(motorcycles)

# Replacing an element in a list
motorcycles[0]= 'Ducati'
print(motorcycles)

# Appending new element to a list
motorcycles.append('Lamborghini')
print(motorcycles)

#Inserting new element by specifying index location
motorcycles.insert(0, 'Mahindra')
motorcycles.insert(2, 'BMW')
print(motorcycles)

# Deleting an element using index 
del motorcycles[0]
print(motorcycles)
popped_motorcycle= motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(motorcycles)
first_motorcycle=motorcycles.pop(0)
print(motorcycles)
print(f"My first motorcycle is {first_motorcycle.title()}")

# Removing item in the list using it's value
print(motorcycles)
too_expensive='Ferrari'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"{too_expensive.title()} is too expensive, so removing from the list fo cars.")