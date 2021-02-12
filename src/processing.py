from bs4 import BeautifulSoup


def get_apple_music_tracks(path):
    with open(path) as file:
        data = BeautifulSoup(file, "xml")

    song_names = data.find_all("key", string="Name")
    artist_names = data.find_all("key", string="Artist")
    titles = []
    artists = []

    for title in song_names:
        titles.append(str(title.next_sibling)[8:-9])

    for artist in artist_names:
        artists.append(str(artist.next_sibling)[8:-9])

    return zip(titles, artists)
