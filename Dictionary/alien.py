alien_0 = {} #Declaring empty dictionary
print(alien_0)

#Assinging kay-values to empty dictionary
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#Updating values in dictionary
print(f"The alien is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

alien_0={'x_position': 5, 'y_position': 0, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#Alien is moving right
#Determine the position of the alien based on its speed
if alien_0['speed'] == 'slow':
    alien_0['x_position'] = alien_0['x_position'] + 1
elif alien_0['speed'] == 'medium':
    alien_0['x_position'] += 2
elif alien_0['speed'] == 'fast':
    alien_0['x_position'] += 3

print(f"New position: {alien_0['x_position']}")

#Deleting in a dictionary
alien_0 = {"color": "green", "points": 5}
del alien_0['points']
print(alien_0)
print(alien_0.get('points', 'Point is not available')) #Get() method in dictionary
