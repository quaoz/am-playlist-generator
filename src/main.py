import time

from fetch import get_details
from fetch import get_network
from processing import get_apple_music_tracks
from write import add_groups
from write import add_tags
from write import file_fixer
from write import get_data
from write import to_file


def get_track_data(songs, path):
    get_network()

    soup = get_data(path=path)
    data = add_groups(soup)

    new_path = path[:-4] + "new.xml"
    to_file(data, new_path)

    data = get_data(new_path)

    for item in songs:
        track, tags = get_details(artist=item[1], title=item[0])
        data = add_tags(data=data, title=track.title, tags=tags)

    processed_data = file_fixer(data)
    to_file(processed_data, new_path)


def main(path):
    start = time.time()

    songs = get_apple_music_tracks(path=path)
    get_track_data(songs=songs, path=path)

    end = time.time()
    print(f"\nTook {end - start} seconds to get the data.\n")


if __name__ == "__main__":
    main(path=input("Input the path to your playlists xml file: "))
