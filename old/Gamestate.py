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

# SOOOO...When you change location of the player, use update location and it will save that location
# according to the path
# Example Usage: update_location(player, "dinuks_house", dinuks_house)
def update_location(player, new_location, next_function):
    player.location = new_location
    if player.path == "forest_path":
        update_last_forest_location(player,new_location)
    next_function(player)

def update_last_forest_location(player, location):
    player.last_forest_location = location


# Makes sure the option the User enter (a number or word) is actually an option. If not, it wil clear screen
# and request user to retry
"""# Example Usage: fp_7 = get_valid_input("You can:\n1. Eat\n2. Drink", [1, 2])
    if fp_7 == 1:
        update_location(player, "eat", eat)
    elif fp_7 == 2:
        update_location(player, "drink", drink)"""



# Clears the screen. THIS IS NOT USED INDIVIDUALLY
# NOTE: os.system cls/clear didn't work so i had to do this...Try to see if u can fix
def clear_screen():
    print("\n" * 100)

