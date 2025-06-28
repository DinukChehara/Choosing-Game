from Player import Player, update_path
from Utils import delayed_print
from Location_path import location_path

# We could do some more here of course. This is the place you run the code from. From here, it gives the
# user the rules. If you get it to work, you can also check whether mac/OS or Windows to do os.system
def game_initialise():
    print("")
    delayed_print("This is a choice based adventure. Read the text and press the given number to make your choice!", 1.5, 0)
    delayed_print("Remember, deaths make you lose all attributes!", 1.5, 0)
    delayed_print("When you reach the next stage, your game will be saved.", 3, 2)
    player = Player()

    # Will Lead to Location path...
    while True:
        update_path(player, location_path)


while True:
    game_initialise()