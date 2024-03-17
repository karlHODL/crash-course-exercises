def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nProvide album details.")
    print("(enter 'q' at any time to quit)")
    title = input("Album title: ")
    if title == 'q':
        break

    artist = input("Artist: ")
    if artist == 'q':
        break

    response = input("Would you like to provide the number of tracks? (y/n) ")
    if response == 'y':
        tracks = input("Number of Tracks: ")
        if tracks == 'q':
            break
    else:
        tracks = None

    album = make_album(artist, title, tracks)
    print(album)