import time
from Utils import delayed_print, get_valid_input
from City_path import city_path
from Restart_Player import handle_death, restart

def forest_path(player):
    delayed_print("You decide to enter the Forest. A small opening in the trees reveal a path.", 1, 0)
    delayed_print("The path goes in on in a direction that will eventually lead you to the City.", 1, 0)
    delayed_print("However, the soft crunch of leaves on your left grabs your attention!", 1, 1)

    # Want to make this a timed challenge somehow where if you take  too long, you die

    start_time = time.time()
    fp_1 = get_valid_input("Think Fast! Will you:\n1. Confront the danger\n2. Run", [1, 2])
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time > 13:
        delayed_print("You took too long...", 2, 1)
        player.update_location("secret_path", secret_path)
    else:
        if fp_1 == 1:
            player.update_location("confront_path", confront_path)
        elif fp_1 == 2:
            player.update_location("avoid_path", avoid_path)

def confront_path(player):
    delayed_print("'Reveal yourself if you dare!' You shout out bravely.", 2, 0)
    delayed_print("You hear the sound of twigs snapping as whatever it was retreats.", 2, 1)
    player.update_courage(is_courageous=True)
    player.update_location("continuing_path", continuing_path)

def avoid_path(player):
    delayed_print("You sprint away. Whatever was spying on you has been left far behind...", 2, 1)
    player.update_courage(is_courageous=False)
    player.update_location("continuing_path", continuing_path)

def continuing_path(player):
    delayed_print("As you continue walking down the path, you come up against a crossroads.")
    get_valid_input("Where will you go?\n1. Left\n2. Right", [1, 2])

def secret_path(player):
    pass