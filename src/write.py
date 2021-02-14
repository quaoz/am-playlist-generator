from bs4 import BeautifulSoup


# reads in the apple music xml file using beautiful soups xml parser
def get_data(path):
    with open(path) as file:
        soup = BeautifulSoup(file, "lxml", from_encoding="UTF-8")

    return soup


def add_tags(data, title, tags):
    song = data.find("string", string=title)
    parent = song.parent
    grouping = parent.find("key", string="Grouping")

    formatted_tags = ""

    for tag in tags:
        formatted_tags += tag + ", "

    formatted_tags = formatted_tags[:-2]

    grouping = grouping.next_sibling
    grouping.string = formatted_tags

    return data


def to_file(split_data, path):
    with open(path, "w+") as file:
        for line in split_data:
            file.write(line + "\n")


def file_fixer(data):
    data = str(BeautifulSoup.decode(data, pretty_print=False, eventual_encoding="UTF-8"))

    data_split = data.split("\n")
    header = data_split[0].split(">", 1)
    data_split.insert(1, header[1])
    data_split[0] = header[0] + ">"

    data_split[2] = data_split[2].replace("<html><body>", "")

    data_length = len(data_split) - 1
    data_split[data_length] = ""

    return data_split


def add_groups(data):
    data = str(BeautifulSoup.decode(data, pretty_print=False, eventual_encoding="UTF-8"))
    data_split = data.split("\n")

    for line in data_split:
        if "<key>Name</key>" in line:
            if "<key>Grouping</key>" not in data_split[data_split.index(line) + 5]:
                data_split.insert(data_split.index(line) + 5, "<key>Grouping</key><string></string>")

    return data_split
