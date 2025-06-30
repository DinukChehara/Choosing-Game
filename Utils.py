import time
import importlib

# prints a message with a delay and blank lines
def delayed_print(message="", delay=1.5, blank_lines=1):
    print(message)
    time.sleep(delay)
    if blank_lines > 0:
        print("\n" * blank_lines, end="")

def get_valid_input(prompt, valid_choices):
    while True:
        prompt += "\n\nYou Pick: "
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
    delayed_print("This will check that everything is working as expected", 2)
    print("Player Check:")
    print(f"  Name: {getattr(player, 'name', 'N/A')}")
    print(f"  Location: {getattr(player, 'location', 'N/A')}")
    print(f"  Path: {getattr(player, 'path', 'N/A')}")
    print(f"  Attributes: {getattr(player, 'attributes', 'N/A')}")
    print(f"  Items: {getattr(player, 'items', 'N/A')}")