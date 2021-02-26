class Home:
    # Attributes
    price = district = rooms = baths = size = floor = url = None

    # Constructor
    def __init__(self, url, district):
        self.district = district
        self.url = url
