def full_dictionary(first, last, middle=''):
    if middle:
        name_details = {"first": first, "middle": middle, "last": last}
    else:
        name_details = {'first': first, 'last': last}
    return name_details


result = full_dictionary("Raj", "Kumar")
print(result)

result = full_dictionary("Raj", "Kumar", "Chandra")
print(result)