name =' Hilton raj '
print(f"Hello {name}, do you want to learn Python?")

# strip
print(name.strip())
# left strip
print(f"Hello {name.lstrip()}, do you want to learn Python?")
# right strip
print(f"Hello {name.rstrip()}, do you want to learn Python?")
# both side strip
print(f"Hello {name.strip()}, do you want to learn Python?")

# title
print(f"Hello {name.title()}, do you want to learn Python?")
# uppercase
print(f"Hello {name.upper()}, do you want to learn Python?")
# lowercase
print(f"Hello {name.lower()}, do you want to learn Python?")

# format 
print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')
famous_person= 'Albert Einstein'
print(f'{famous_person} once said, “A person who never made a mistake never tried anything new.”')

# remove suffix
file = 'python.docx'
print(f'I store all my notes in a word document named "{file.removesuffix(".docx")}"')
# remove prefix
website='www.google.com'
print(f'Webiste: {website.removeprefix("www.")}')