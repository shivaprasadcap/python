alien_0 = {"color": "green", "points": 5}  # Declaring dictionary.
print(alien_0["color"])  # printing value form dictionary.
print(alien_0["points"])

# Using values in a print statement
points = alien_0[
    "points"
]  # Need to initialize to a variable to use in print statement.
print(f"You have gained {points} points!")

# Printing using list comprehension
[print(values) for values in alien_0.values()]

# Displaying values using for loop
for values in alien_0:
    print(values)

# Storing values of a dictionary in a list
list_of_values = list(alien_0.values())
print(list_of_values)

# Adding a new key-value pair to the dictionary
alien_0["x_position"] = 0  # Just consider key as index position
alien_0["y_position"] = 25
print(alien_0)


# Always use double inverted comma to display a value in a print statement
print(f"You have gained {alien_0['points']}")


