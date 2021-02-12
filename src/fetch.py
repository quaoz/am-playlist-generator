import os

import pylast
from dotenv import load_dotenv


def get_track(artist, title):
    track = network.get_track(artist=artist, title=title)

    return track


# return the album of a track
def get_album(track):
    album = track.get_album()
    return album


# return the tags of a track that are above a certain weight
def get_tags(track, minimum_weight, maximum_tags, minimum_tags):
    top_tags = track.get_top_tags(limit=maximum_tags)
    tags = []

    # checks that the tags are above the minimum accepted weight
    for top_tag in top_tags:
        if int(top_tag.weight) >= minimum_weight:
            tags.append(top_tag.item.get_name())

        # if the tags are bellow the accepted weight but the minimum number hasn't been met it will add them anyway
        elif len(tags) <= minimum_tags:
            tags.append(top_tag.item.get_name())

        else:
            break

    return tags


def get_details(artist, title, tag_minimum_weight=50, maximum_tags=10, minimum_tags=3):
    track = get_track(artist=artist, title=title)
    tags = get_tags(track, minimum_weight=tag_minimum_weight, maximum_tags=maximum_tags, minimum_tags=minimum_tags)

    return track, tags


# creates the network object using the key and secret from the keys.env file
def get_network():
    # read in the last.fm key and secret from a file
    load_dotenv("keys.env")
    api_key = os.getenv(key="API_KEY")
    api_secret = os.getenv(key="API_SECRET")

    global network
    network = pylast.LastFMNetwork(
        api_key=api_key,
        api_secret=api_secret
    )
