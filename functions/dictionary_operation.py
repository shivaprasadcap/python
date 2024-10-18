def name(first, last, age=None):
    full_details = {'first': first, "last": last}

    if age:
        full_details['age'] = age
    
    return full_details

person = name("Raj", "Kumar")
print(person)

person = name("Raj", "Kumar", 21)
print(person)