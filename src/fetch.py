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
def get_tags(track, minimum_weight, tag_limit):
    top_items = track.get_top_tags(limit=tag_limit)
    tags = []

    for top_item in top_items:
        if int(top_item.weight) >= minimum_weight:
            tags.append(top_item.item.get_name())

        else:
            break

    return tags


def get_details(artist, title, tag_minimum_weight=50, tag_limit=10):
    track = get_track(artist=artist, title=title)
    tags = get_tags(track, minimum_weight=tag_minimum_weight, tag_limit=tag_limit)

    return track, tags


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
