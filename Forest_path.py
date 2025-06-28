import time
from Utils import delayed_print, get_valid_input
from Player import update_path, update_location
from City_path import city_path
from Restart_Player import handle_death, restart

def forest_path(player):
    delayed_print("You decide to enter the Forest. A small opening in the trees reveal a path.", 2, 0)
    delayed_print("The path goes in on in a direction that will eventually lead you to the City.", 2, 0)
    delayed_print("However, the soft crunch of leaves on your left grabs your attention!", 1.5, 1)

    # Want to make this a timed challenge somehow where if you take  too long, you die

    start_time = time.time()
    fp_1 = get_valid_input("Think Fast! Will you:\n1. Confront the danger\n2. Run", [1, 2])
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time > 5:
        delayed_print("You took too long...", 2, 1)
        update_location(player, secret_path)
    else:
        if fp_1 == 1:
            update_location(player, confront_path)
        elif fp_1 == 2:
            update_location(player, avoid_path)

# Leads back to
def confront_path(player):
    delayed_print("'Reveal yourself if you dare!' You shout out bravely.", 2, 0)
    delayed_print("You hear the sound of twigs snapping as whatever it was retreats.", 2, 1)
    player.update_courage(is_courageous=True)
    update_location(player, continuing_path)

def avoid_path(player):
    delayed_print("You sprint away. Whatever was spying on you has been left far behind...", 2, 1)
    update_location(player, confront_path)

def continuing_path(player):
    pass

def secret_path(player):
    pass