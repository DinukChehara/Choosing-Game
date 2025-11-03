from Utils import delayed_print, get_valid_input, import_path
import random

# This is what it will look like basically. So if you have unlocked this path (you can unlock a path by
# reaching it, for example, going from city to forest), and you select that option, then you can go to
# that path. Now if you reach another path and then SAVE the game, the same thing should happen.
# It needs an improvement for sure tho

def location_path(player):
    delayed_print("You are walking down a small road but...", 1, 0)
    delayed_print("You don't seem to be able to remember anything else...", 1, 0)
    delayed_print("The Mountain road you been following for...a few hours?", 1, 1)
    delayed_print("You must enter the city but the guards in front of that gate don't look friendly.", 1, 0)
    delayed_print("The swamp contains some of the most dangerous animals in the kingdom...", 1, 0)
    delayed_print("And the mountains where you came from are- wait. Best not talk about that...", 1, 1)

    if player.unlocks["mountain"]:
        fp_1 = get_valid_input("1. The Forest\n2. The City\n3. The Swamp\n4. The Mountains ",[1, 2, 3, 4])
    elif player.unlocks["swamp"]:
        fp_1 = get_valid_input("1. The Forest\n2. The City\n3. The Swamp\n4. The Mountains (Locked) ",[1, 2, 3, 4])
    elif player.unlocks["city"]:
        fp_1 = get_valid_input("1. The Forest\n2. The City\n3. The Swamp (Locked)\n4. The Mountains (Locked) ",[1, 2, 3, 4])
    else:
        fp_1 = get_valid_input("1. The Forest\n2. The City (Locked)\n3. The Swamp (Locked)\n4. The Mountains (Locked) ",[1, 2, 3, 4])

    print("")

    if fp_1 == 1:
        import_path(player, "forest")

    elif fp_1 == 2:
        if not player.unlocks["city"]:
            city_rebuff = ["As you approach the great City walls, the guards sneer at you. You decide to back off...",
                             "As you approach the great City walls, the guard shouts: 'No visitors at this hour!'.\nYou slowly back off...",
                             "The guards move away and you try to enter the city, but the gates are locked. You'll have to find another way in.",
                             "The city is bustling with activity, but the guards won't let you in. You'll have to try again later.",
                             "You're not allowed in the city right now. Maybe you can find a way to unlock it later."]
            rand_forest = random.choice(city_rebuff)
            delayed_print(f"{rand_forest}", 3, 1)
        else:
            import_path(player, "city")

    elif fp_1 == 3:
        if not player.unlocks["swamp"]:
            swamp_rebuff = ["You begin to enter but your foot immediately sinks in to the mushy ground. You nearly pull your foot out trying to get out...",
                           "As you step into the swamp, you sink into the mud up to your knees. You're not going anywhere.",
                           "The swamp is treacherous, and you're not prepared to face its dangers. You turn back.",
                           "You try to enter the swamp, but the trees seem to close in around you. You're not welcome here.",
                           "The swamp is home to many dangers, and you're not ready to face them. Come back later."]
            rand_city = random.choice(swamp_rebuff)
            delayed_print(f"{rand_city}", 3, 1)
        else:
            import_path(player, "swamp")

    elif fp_1 == 4:
        if not player.unlocks["mountain"]:
            mountain_rebuff = ["The mountain path is steep and rocky, and you're not sure you can make it.",
                "As you start up the mountain, you hear the howl of wolves dangerously close by. You turn back.",
                "The mountain is shrouded in mist, and you can't a thing. You'll have to wait for a clearer day.",
                "You try to enter the mountain, but something in you tells you that it is a terrible idea.",
                "The mountain is home to many dangers, and you're not ready to face them. Come back later."]
            rand_mountain = random.choice(mountain_rebuff)
            delayed_print(f"{rand_mountain}", 3, 1)
        else:
            import_path(player, "mountain")

