from Location import Location


class Game:
    def __init__(self):
        self.__locations : list[Location] = [Location("Forest"), Location("City"), Location("House")]

    def getLocations(self):
        return self.__locations