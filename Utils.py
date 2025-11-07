import time
import importlib

# prints a message with a delay and blank lines
def delayed_print(message="", delay=2, blank_lines=0):
    print(message)
    time.sleep(delay)
    if blank_lines > 0:
        print("\n" * blank_lines, end="")

def get_valid_input(prompt, valid_choices):
    prompt += "\n\nYou Pick: "
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            else:
                raise ValueError
        except ValueError:
            clear_screen()
            time.sleep(1)
            print(f"Invalid input. Please choose from {valid_choices}.")

def clear_screen():
    print("\n" * 100)

def import_path(player, path):
    normalized = path.lower()
    capitalized = normalized.capitalize()
    player.path = f"{normalized}_path"
    module = importlib.import_module(f"{capitalized}_path")
    func = getattr(module, f"{normalized}_path")
    func(player)

def error_check(player):
    delayed_print("This will check that everything is working as expected", 2, 1)
    delayed_print("Player Check:", 2)
    delayed_print(f"  Name: {getattr(player, 'name', 'N/A')}", 2)
    delayed_print(f"  Location: {getattr(player, 'location', 'N/A')}", 2)
    delayed_print(f"  Path: {getattr(player, 'path', 'N/A')}", 2)
    delayed_print(f"  Attributes: {getattr(player, 'attributes', 'N/A')}", 2)
    delayed_print(f"  Items: {getattr(player, 'items', 'N/A')}", 2, 1)
    delayed_print("Check complete. If you see any unexpected result, fix it. N/A is nothing to worry about.", 3)
    delayed_print("Unless the player s supposed have an item/attribute....", 3, 1)

