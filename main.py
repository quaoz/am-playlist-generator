import pylast
import os
from dotenv import load_dotenv


def get_track():
    artist = input("Artist: ")
    title = input("Title: ")

    # Try to resolve the track, work in progress
    try:
        track = network.get_track(artist, title)
        track.get_album()

    except pylast.WSError:
        print("Trying to resolve track... (Method 1)")
        corrected_artist = track.get_artist().get_correction()

        try:
            track = network.get_track(corrected_artist, title)
            track.get_album()

        except pylast.WSError:
            print("Trying to resolve track... (Method 2)")

            try:
                corrected_title = track.get_title(properly_capitalized=True)
                track = network.get_track(artist, corrected_title)
                track.get_album()

            except pylast.WSError:
                print("Trying to resolve track... (Method 3)")

                try:
                    track = network.get_track(corrected_artist, corrected_title)
                    track.get_album()

                except pylast.WSError:
                    print("Trying to resolve track... (Method 4)")

                    try:
                        track = network.get_track(title=title)
                        track.get_album()

                    except pylast.WSError:
                        print("Trying to resolve track... (Method 5)")

                        try:
                            track = network.get_track(title=corrected_title)
                            track.get_album()

                        except pylast.WSError:
                            print("Unable to find track")
                            quit()

    return track


# return the album of a track
def get_album(track):
    album = track.get_album()
    return album


# return the tags of a track that are above a certain weight
def get_tags(track, minimum_weight):
    top_items = track.get_top_tags(limit=None)
    tags = []

    for top_item in top_items:
        if int(top_item.weight) >= minimum_weight:
            tags.append(top_item.item.get_name())
            print(f"Tag: {top_item.item.get_name()}, Weight: {top_item.weight}")
        else:
            break

    return tags


def main():
    track = get_track()
    print(f"Track: {track}")

    album = get_album(track)
    print(f"Album: {album}")

    top_tags = get_tags(track, 45)


if __name__ == "__main__":
    # read in the last.fm key and secret from a file
    load_dotenv('keys.env')
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")

    network = pylast.LastFMNetwork(
        api_key=API_KEY,
        api_secret=API_SECRET
    )

    main()
