
class Player:
    def __init__(self):
        self.location = None
        self.path = None

    def updateLocation(self, location):
        self.location = location

    def updatePath(self, path):
        self.path = path

    def