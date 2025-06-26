import time

class Player:
    def __init__(self):
        self.location = ""
        self.path = ""


# So, this basically just updates the path of the player.
#Example Usage: update_path(player, "location_path", location_path)
def update_path(player, new_path, next_function):
    player.path = new_path
    next_function(player)

# SOOOO...When you change location of the player, use update location, and it will save that location
# according to the path
# Example Usage: update_location(player, "dinuks_house", dinuks_house)
def update_location(player, new_location, next_function):
    player.location = new_location
    if player.path == "forest_path":
        update_last_forest_location(player,new_location)
    next_function(player)

def update_last_forest_location(player, location):
    player.last_forest_location = location