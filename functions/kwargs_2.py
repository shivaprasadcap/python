def make_car(name, type, **kwargs):
    print('Please find below the specification of the car: ')
    print(f'Name: {name}')
    print(f'Type: {type}')

    for key, value in kwargs.items():
        print(f"{key.title()}: {value.title()}")

make_car('Toyota', 'Good', model= 'Sport', seater= '4', ratings= '3')