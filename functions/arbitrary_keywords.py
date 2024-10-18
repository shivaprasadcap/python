def make_profile(first, last, **user_profile):
    
    user_profile['first_name'] = first
    user_profile['last_name'] = last

    return user_profile

profile = make_profile('Shiva', 'Prasad', age = 24, location = 'Bangalore', occupation = 'Engineer')
print(profile)
