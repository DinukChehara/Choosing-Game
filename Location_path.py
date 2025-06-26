from Utils import delayed_print, get_valid_input
from Player import update_path
from Forest_path import forest_path

# This is what it will look like basically. So if you have unlocked this path (you can unlock a path by
# reaching it for example going from city to forest), and you select that option, then you can go to
# that path. Now if you reached another path and then SAVE the game, same thing should happen.
# It needs an improvement for sure tho

def location_path(player):
    delayed_print("You open your eyes. You don't know where you are but you see four possible places to go.", 1, 0)

    if player.unlocks["pond"]:
        fp_1 = get_valid_input("1. The Woods\n2. The City\n3. The Mountains\n4. The Pond ",[1, 2, 3, 4])
    elif player.unlocks["house"]:
        fp_1 = get_valid_input("1. The Woods\n2. The City\n3. The Mountains\n4. The Pond (Locked) ",[1, 2, 3])
    elif player.unlocks["city"] or player.get_save_slot_count(player) > 0:
        fp_1 = get_valid_input("1. The Woods\n2. The City\n3. The Mountains (Locked)\n4. The Pond (Locked) ",[1, 2])
    else:
        fp_1 = get_valid_input("1. The Woods\n2. The City (Locked)\n3. The Mountains (Locked)\n4. The Pond (Locked) ",[1])
    print("")

    if fp_1 == 1:
        import Forest_path
        update_path(player, "forest_path", Forest_path.forest_path)
    elif fp_1 == 2:
        import City_path
        update_path(player, "city_path", City_path.city_path)
    elif fp_1 == 3:
        import Marsh_path
        update_path(player, "marsh_path", Marsh_path.marsh_path)
    elif fp_1 == 4:
        import Mountain_path
        update_path(player, "mountain_path", Mountain_path.mountain_path)

