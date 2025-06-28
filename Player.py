import time
import json

from Utils import delayed_print

class Player:
    def __init__(self):
        self.attributes = {"courage": False, "coward": False, "smart": False, "foolish": False}
        self.forest_attributes = {"courage": False, "coward": False, "smart": False, "foolish": False}
        self.city_attributes = {"courage": False, "coward": False, "smart": False, "foolish": False}

        self.forest_items = {}
        self.city_items = {}

        self.visited_forest_locations = {}
        self.visited_city_locations = {}

        self.unlocks = {"city": False, "mountain": False, "swamp": False}
        self.location = ""
        self.path = ""
        self.last_forest_location = ""

    # For ONLY the self.attributes
    def update_attributes(self, attribute, value):
        if attribute in self.attributes:
            self.attributes[attribute] = value

    # Needed for when player dies
    def reset_attributes(self):
        for key in self.attributes:
            self.attributes[key] = False

    # Same thing
    def update_forest_attributes(self, attribute, value):
        if attribute in self.forest_attributes and self.path == "forest_path":
            self.forest_attributes[attribute] = value
    def reset_forest_attributes(self):
        for key in self.forest_attributes:
            self.forest_attributes[key] = False

    def update_city_attributes(self, attribute, value):
        if attribute in self.city_attributes and self.path == "forest_path":
            self.city_attributes[attribute] = value
    def reset_city_attributes(self):
        for key in self.city_attributes:
            self.city_attributes[key] = False


    def reset_visited_forest_locations(self):
        for key in self.visited_forest_locations:
            self.visited_forest_locations[key] = False
    def update_visited_forest_locations(self, location, value):
        if location in self.visited_forest_locations:
            self.visited_forest_locations[location] = value

    def reset_visited_city_locations(self):
        for key in self.visited_city_locations:
            self.visited_city_locations[key] = False
    def update_visited_city_locations(self, location, value):
        if location in self.visited_city_locations:
            self.visited_city_locations[location] = value

    def update_courage(self, is_courageous):
        if is_courageous:
            self.update_attributes("courage", True)
            self.update_attributes("coward", False)

            if self.path == "forest_path":
                self.update_forest_attributes("courage", True)
                self.update_forest_attributes("coward", False)

            elif self.path == "city_path":
                self.update_city_attributes("courage", True)
                self.update_city_attributes("coward", False)

            delayed_print("You feel Courageous.", 1, 1)

        else:
            self.update_attributes("courage", False)
            self.update_attributes("coward", True)

            if self.path == "forest_path":
                self.update_forest_attributes("courage", False)
                self.update_forest_attributes("coward", True)

            elif self.path == "city_path":
                self.update_city_attributes("courage", False)
                self.update_city_attributes("coward", True)

            delayed_print("You start to feel cowardly.", 1, 1)
    def update_smart(self, is_intelligent):
        if is_intelligent:
            self.update_attributes("smart", True)
            self.update_attributes("foolish", False)

            if self.path == "forest_path":
                self.update_forest_attributes("smart", True)
                self.update_forest_attributes("foolish", False)

            elif self.path == "city_path":
                self.update_city_attributes("smart", True)
                self.update_city_attributes("foolish", False)

            delayed_print("You feel Intelligent.", 1,1)
        else:
            self.update_attributes("smart", False)
            self.update_attributes("foolish", True)

            if self.path == "forest_path":
                self.update_forest_attributes("smart", False)
                self.update_forest_attributes("foolish", True)

            elif self.path == "city_path":
                self.update_city_attributes("smart", False)
                self.update_city_attributes("foolish", True)

            delayed_print("You start to feel Foolish.", 1, 1)

    # Used for Updating and resetting all items
    def reset_forest_items(self):
        for key in self.forest_items:
            self.forest_items[key] = False
    def update_forest_items(self, item, value):
        if item in self.forest_items:
            self.forest_items[item] = value

    def reset_city_items(self):
        for key in self.city_items:
            self.city_items[key] = False
    def update_city_items(self, item, value):
        if item in self.city_items:
            self.city_items[item] = value

# So, this basically just updates the path of the player.
#Example Usage: update_path(player, "location_path", location_path)
def update_path(player, new_path):
    player.path = str(new_path)
    new_path(player)

# SOOOO...When you change the location of the player, use update location, and it will save that location
# according to the path
# Example Usage: update_location(player, "dinuks_house", dinuks_house)
def update_location(player, new_location):
    player.location = str(new_location)
    if player.path == "forest_path":
        update_last_forest_location(player,new_location)
    elif player.path == "city_path":
        update_last_city_location(player,new_location)
    new_location(player)

def update_last_forest_location(player, location):
    player.last_forest_location = location

def update_last_city_location(player, location):
    player.last_city_location = location