from bs4 import BeautifulSoup


# reads in the apple music xml file using beautiful soups xml parser
def get_data(path):
    with open(path) as file:
        data = BeautifulSoup(file, "xml")

    return data


# extracts the artists and song titles from the xml file
def get_apple_music_tracks(path):
    data = get_data(path=path)

    song_names = data.find_all("key", string="Name")
    artist_names = data.find_all("key", string="Artist")

    titles = []
    artists = []

    for title in song_names:
        titles.append(str(title.next_sibling)[8:-9])

    for artist in artist_names:
        artists.append(str(artist.next_sibling)[8:-9])

    return zip(titles, artists)
