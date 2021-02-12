import time

from fetch import get_album
from fetch import get_details
from fetch import get_network
from processing import get_apple_music_tracks


def get_tracks(path):
    start = time.time()
    songs = get_apple_music_tracks(path=path)

    end = time.time()
    print(f"\nTook {end - start} seconds to read the data.\n\n")

    return songs


def get_track_data(songs):
    get_network()

    for item in songs:
        track, tags = get_details(artist=item[1], title=item[0])
        print(f"Track: {track}")

        album = get_album(track=track)
        print(f"Album: {album}")

        print("Tags: ")
        for tag in tags:
            print(f" -{tag}")

        print("\n")


def main(path):
    songs = get_tracks(path=path)
    get_track_data(songs=songs)


if __name__ == "__main__":
    main(path=input("Input the path to your playlists xml file"))
