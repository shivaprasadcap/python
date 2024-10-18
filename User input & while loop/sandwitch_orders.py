sandwitch_orders = ['pastami sandwitch', 'panner sandwitch', 'pastami sandwitch', 'cheese sandwitch', 'pastami sandwitch', 'chicken sandwitch']
finished_sandwitches = []

print('Pastami sandwicthes are out of stock!')
while 'pastami sandwitch' in sandwitch_orders:
    sandwitch_orders.remove('pastami sandwitch')
    
while sandwitch_orders:
    sandwitch = sandwitch_orders.pop()
    print(f'\nI made your {sandwitch.title()}.')

    finished_sandwitches.append(sandwitch)

print('\nList of finished Sandwitches:')
for sandwitch in finished_sandwitches:
    print(sandwitch.title())