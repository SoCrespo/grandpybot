# coding: utf-8

class Place:
    """
    Place object : name, address, place_id.
    """

    def __init__(self, name, address, place_id):
        self.name = name
        self.address = address
        self.place_id = place_id
        self.text = None
        self.url = None
        self.map = None

if __name__ == "__main__":
    pass