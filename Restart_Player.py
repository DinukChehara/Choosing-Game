from Utils import clear_screen, delayed_print, import_path

def restart(player):
    while True:
        if player.path == "forest_path":
            return restart_forest_path(player)
        elif player.path == "city_path":
            return restart_city_path(player)
        elif player.path == "swamp_path":
            return restart_swamp_path(player)
        elif player.path == "mountain_path":
            return restart_mountains_path(player)


def yes_no_input(prompt):
    while True:
        response = input(prompt).lower().strip()
        if response in ["y", "n"]:
            return response
        else:
            print("Invalid input...Try again.")

# restart(player) will lead to either of the based on what path the player is in, will clear the screen
# and reset attributes, items and location

def restart_forest_path(player):
    player.reset_attributes()
    player.reset_forest_attributes()
    player.location = ""
    player.reset_forest_items()
    player.reset_visited_forest_locations()

    response = yes_no_input("Restart from beginning? y/n")
    clear_screen()
    if response == "y":
        from Location_path import location_path
        delayed_print("Restarting...", 1, 0)
        player.update_path("location_path", location_path)
    elif response == "n":
        import_path(player, "forest_path")

def restart_city_path(player):
    player.reset_attributes()
    player.reset_visited_city_locations()
    player.reset_city_attributes()
    player.reset_city_items()

    response = yes_no_input("Restart from beginning? y/n")
    clear_screen()

    if response == "y":
        from Location_path import location_path
        delayed_print("Restarting...", 1, 0)
        player.location = ""
        player.update_path("location_path", location_path)

    elif response == "n":
        import_path(player, "city_path")

def restart_swamp_path(player):
    response = yes_no_input("Restart from beginning? y/n")
    clear_screen()

    if response == "y":
        from Location_path import location_path
        delayed_print("Restarting...", 1, 0)
        player.update_path("location_path", location_path)
    elif response == "n":
        import_path(player, "swamp_path")

def restart_mountains_path(player):
    response = yes_no_input("Restart from beginning? y/n")
    clear_screen()

    if response == "y":
        from Location_path import location_path
        delayed_print("Restarting...", 1, 0)
        player.update_path("location_path", location_path)
    elif response == "n":
        import_path(player, "mountain_path")


def handle_death(player, message, restart_function):
    delayed_print(message)
    restart_function(player)