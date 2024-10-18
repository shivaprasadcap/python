def make_album(artist, title):
    # print(f"Artist name: {artist.title()}")
    # print(f"Title: {title.title()}")
    content = {'artist': artist, 'title': title}
    print(content)

while True:
    print("Enter Artist and Album names: ")
    print("Enter 'q' anytime to quit.")
    artist = input("Enter artist's name: ")
    if artist == 'q':
        break
    title = input("Enter album title: ")
    if title == 'q':
        break

    make_album(artist, title)

