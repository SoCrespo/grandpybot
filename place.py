# coding: utf-8

class Place:
    """
    Place object : name, address, place_id.
    """

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.wiki_text = None
        self.wiki_url = None
        self.map = None

if __name__ == "__main__":
    pass