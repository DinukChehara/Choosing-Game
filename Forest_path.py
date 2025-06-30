import time
from Utils import delayed_print, get_valid_input
from Player import update_path, update_location
from City_path import city_path
from Restart_Player import handle_death, restart

def forest_path(player):
    delayed_print("You decide to enter the Forest. A small opening in the trees reveal a path.", 1, 0)
    delayed_print("The path goes in on in a direction that will eventually lead you to the City.", 1, 0)
    delayed_print("However, the soft crunch of leaves on your left grabs your attention!", 1, 1)

    # Want to make this a timed challenge somehow where if you take  too long, you die

    start_time = time.time()
    fp_1 = get_valid_input("Think Fast! Will you:\n1. Confront the danger\n2. Run\n3. Test the Code out", [1, 2, 3])
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time > 13:
        delayed_print("You took too long...", 2, 1)
        update_location(player, "secret_path", secret_path)
    else:
        if fp_1 == 1:
            update_location(player, "confront_path", confront_path)
        elif fp_1 == 2:
            update_location(player, "avoid_path", avoid_path)
        elif fp_1 == 3:
            update_location(player, "test", test)

def test(player):
    print("Testing")
    player.update_courage(is_courageous=True)
    test_01 =  get_valid_input("1, 2, 3, 4, 5",[1, 2, 3, 4, 5])
    if test_01 == 1:
        update_location(player, "test_1", test_1)
    elif test_01 == 2:
        update_location(player, "test_2", test_2)
    elif test_01 == 3:
        update_location(player, "test_3", test_3)
    elif test_01 == 4:
        update_location(player, "test_4", test_4)
    elif test_01 == 5:
        update_location(player, "test_5", test_5)

def test_1(player):
    player.update_smart(is_intelligent=False)
    update_path(player, "city_path", city_path)

def test_2(player):
    player.update_forest_items("test_item", True)
    update_path(player, "city_path", city_path)
    player.update_visited_forest_locations("test_location_3", True)

def test_3(player):
    player.update_forest_items("test_item_2", True)
    update_path(player, "city_path", city_path)
    player.update_visited_forest_locations("test_location_3", True)

def test_4(player):
    player.update_visited_forest_locations("test_location_2", True)
    player.update_forest_items("test_item_3", True)
    update_path(player, "city_path", city_path)

def test_5(player):
    player.update_courage(is_courageous=False)
    player.update_visited_forest_locations("test_location", True)
    update_path(player, "city_path", city_path)

def confront_path(player):
    delayed_print("'Reveal yourself if you dare!' You shout out bravely.", 2, 0)
    delayed_print("You hear the sound of twigs snapping as whatever it was retreats.", 2, 1)
    player.update_courage(is_courageous=True)
    update_location(player, "continuing_path", continuing_path)

def avoid_path(player):
    delayed_print("You sprint away. Whatever was spying on you has been left far behind...", 2, 1)
    player.update_courage(is_courageous=False)
    update_location(player, "continuing_path", continuing_path)

def continuing_path(player):
    delayed_print("As you continue walking down the path, you come up against a crossroads.")
    get_valid_input("Where will you go?\n1. Left\n2. Right", [1, 2])

def secret_path(player):
    pass