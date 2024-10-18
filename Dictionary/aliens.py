alien_0 = {
    'color': 'green',
    'points': 5,
}

alien_1 = {
    'color': 'yellow',
    'points': 10,
}

alien_2 = {
    'color': 'red',
    'points': 15,
}

aliens = [alien_0, alien_1, alien_2]
print(aliens)

for alien in aliens:
    print(alien)


#A list of dictionaries
aliens =[]

for alien in range(30): #Creating 30 dictionaries inside a list
    new_alien= {
        'color': 'green',
        'points': 5
        }
    aliens.append(new_alien)

for alien in aliens[:5]: #Displaying first 5 dictionaries in the list
    print(alien)
print("...")
print(f"There are {len(aliens)} aliens.")

#Updating some dictionaries in the list
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'fast'
        alien['points'] = 10

for alien in aliens[:3]:
    print (alien)