from Utils import delayed_print, get_valid_input, import_path
from Player import update_path
from Forest_path import forest_path

# This is what it will look like basically. So if you have unlocked this path (you can unlock a path by
# reaching it, for example, going from city to forest), and you select that option, then you can go to
# that path. Now if you reach another path and then SAVE the game, same thing should happen.
# It needs an improvement for sure tho

def location_path(player):
    delayed_print("You are walking down a small road but...", 2, 0)
    delayed_print("You don't seem to be able to remember anything else...", 2, 1)
    delayed_print("The Mountain road you been following for...a few hours?", 2, 0)
    delayed_print("You must enter the city but the guards in front of that gate don't look friendly.", 2, 1)

    if player.unlocks["mountain"]:
        fp_1 = get_valid_input("1. The Forest\n2. The City\n3. The Swamp\n4. The Mountains ",[1, 2, 3, 4])
    elif player.unlocks["swamp"]:
        fp_1 = get_valid_input("1. The Forest\n2. The City\n3. The Swamp\n4. The Mountains (Locked) ",[1, 2, 3])
    elif player.unlocks["city"]:
        fp_1 = get_valid_input("1. The Forest\n2. The City\n3. The Swamp (Locked)\n4. The Mountains (Locked) ",[1, 2])
    else:
        fp_1 = get_valid_input("1. The Forest\n2. The City (Locked)\n3. The Swamp (Locked)\n4. The Mountains (Locked) ",[1])


    if fp_1 == 1:
        import_path(player, "forest_path")
    elif fp_1 == 2:
        import_path(player, "city_path")
    elif fp_1 == 3:
        import_path(player, "swamp_path")
    elif fp_1 == 4:
        import_path(player, "mountain_path")

