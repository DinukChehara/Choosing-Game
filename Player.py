import json, os, types
from Utils import delayed_print

from Utils import delayed_print

saveFileName = "saves.json"

default_data = {
    "slots": {}
}

if not os.path.exists(saveFileName) or os.path.getsize(saveFileName) == 0:
    with open(saveFileName, "w") as f:
        json.dump(default_data, f)

class Player:
    def __init__(self):
        self.attributes = {"courage": False, "coward": False, "smart": False, "foolish": False}
        self.forest_attributes = {"courage": False, "coward": False, "smart": False, "foolish": False}
        self.city_attributes = {"courage": False, "coward": False, "smart": False, "foolish": False}

        self.forest_items = {"Test_1": True, "Test_2": False, "Test_3": False}
        self.city_items = {}

        self.visited_forest_locations = {"Test_1": False, "Test_2": False, "Test_3": False,}
        self.visited_city_locations = {}

        self.unlocks = {"city": False, "mountain": False, "swamp": False}
        self.location = ""
        self.path = ""
        self.last_forest_location = ""

    # For ONLY the self.attributes
    def update_attributes(self, attribute, value):
        if attribute in self.attributes:
            self.attributes[attribute] = value

    # Needed for when player dies
    def reset_attributes(self):
        for key in self.attributes:
            self.attributes[key] = False

    # Same thing
    def update_forest_attributes(self, attribute, value):
        if attribute in self.forest_attributes and self.path == "forest_path":
            self.forest_attributes[attribute] = value
    def reset_forest_attributes(self):
        for key in self.forest_attributes:
            self.forest_attributes[key] = False

    def update_city_attributes(self, attribute, value):
        if attribute in self.city_attributes and self.path == "forest_path":
            self.city_attributes[attribute] = value
    def reset_city_attributes(self):
        for key in self.city_attributes:
            self.city_attributes[key] = False


    def reset_visited_forest_locations(self):
        for key in self.visited_forest_locations:
            self.visited_forest_locations[key] = False
    def update_visited_forest_locations(self, location, value):
        if location in self.visited_forest_locations:
            self.visited_forest_locations[location] = value

    def reset_visited_city_locations(self):
        for key in self.visited_city_locations:
            self.visited_city_locations[key] = False
    def update_visited_city_locations(self, location, value):
        if location in self.visited_city_locations:
            self.visited_city_locations[location] = value

    def update_courage(self, is_courageous):
        if is_courageous:
            self.update_attributes("courage", True)
            self.update_attributes("coward", False)

            if self.path == "forest_path":
                self.update_forest_attributes("courage", True)
                self.update_forest_attributes("coward", False)

            elif self.path == "city_path":
                self.update_city_attributes("courage", True)
                self.update_city_attributes("coward", False)

            delayed_print("You feel Courageous.", 1, 1)

        else:
            self.update_attributes("courage", False)
            self.update_attributes("coward", True)

            if self.path == "forest_path":
                self.update_forest_attributes("courage", False)
                self.update_forest_attributes("coward", True)

            elif self.path == "city_path":
                self.update_city_attributes("courage", False)
                self.update_city_attributes("coward", True)

            delayed_print("You start to feel cowardly.", 1, 1)
    def update_smart(self, is_intelligent):
        if is_intelligent:
            self.update_attributes("smart", True)
            self.update_attributes("foolish", False)

            if self.path == "forest_path":
                self.update_forest_attributes("smart", True)
                self.update_forest_attributes("foolish", False)

            elif self.path == "city_path":
                self.update_city_attributes("smart", True)
                self.update_city_attributes("foolish", False)

            delayed_print("You feel Intelligent.", 1,1)
        else:
            self.update_attributes("smart", False)
            self.update_attributes("foolish", True)

            if self.path == "forest_path":
                self.update_forest_attributes("smart", False)
                self.update_forest_attributes("foolish", True)

            elif self.path == "city_path":
                self.update_city_attributes("smart", False)
                self.update_city_attributes("foolish", True)

            delayed_print("You start to feel Foolish.", 1, 1)

    # Used for Updating and resetting all items
    def reset_forest_items(self):
        for key in self.forest_items:
            self.forest_items[key] = False
    def update_forest_items(self, item, value):
        if item in self.forest_items:
            self.forest_items[item] = value

    def reset_city_items(self):
        for key in self.city_items:
            self.city_items[key] = False
    def update_city_items(self, item, value):
        if item in self.city_items:
            self.city_items[item] = value

    # So, this basically just updates the path of the player.
    # Example Usage: update_path(player, "location_path", location_path)
    def update_path(self, new_path, next_function):
        self.path = new_path
        next_function(self)

    # SO...When you change the location of the player, use update location, and it will save that location
    # according to the path
    # Example Usage: update_location(player, "dinuks_house", dinuks_house)
    def update_location(self, new_location, next_function):
        self.location = new_location
        if self.path == "forest_path":
            self.update_last_forest_location(new_location)
        elif self.path == "city_path":
            self.update_last_city_location(new_location)
        next_function(self)

    # These functions are used to update the last forest and city locations
    def update_last_forest_location(self, location):
        self.last_forest_location = location
    def update_last_city_location(self, location):
        self.last_city_location = location


def save_and_load_menu(player, path_func):
    while True:
        print("Save/Load Menu:")
        print("1. Save Game")
        print("2. Load Game")
        print("3. Continue")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            save_menu(player)
        elif choice == "2":
            load_menu(player, path_func)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def save_menu(player):
    slots = get_save_slots()
    used_slots = len(slots)
    print(f"You have {used_slots}/5 save slots.")
    display_save_slots()
    delayed_print("\n", 0.5, 0)
    while True:
        slot_input = input("Enter a slot number to save to (1-5): ").strip()
        if not slot_input.isdigit() or not (1 <= int(slot_input) <= 5):
            delayed_print("Invalid slot number. Please enter a number between 1 and 5.\n", 0.5, 0)
            continue
        slot = str(int(slot_input))
        slot_name = input("Enter a name for your save slot: ").strip()
        for s, slot_data in slots.items():
            for name, data in slot_data.items():
                if data.get("forest_locations") == player.last_forest_location and s != slot:
                    delayed_print(f"Error: This location is already saved in slot {s} ('{name}'). Choose a different location or slot.\n", 0.5, 0)
                    break
            else:
                continue
            break
        else:
            if slot in slots and slots[slot]:
                print(f"Slot {slot} already has saves:")
                for name in slots[slot]:
                    print(f"  - {name}")
                confirm = input("Are you sure you want to overwrite this slot? (y/n): ").strip().lower()
                if confirm != "y":
                    delayed_print("Cancelled. Please choose a slot again.\n", 0.5, 0)
                    continue
            save_forest_data(player, slot_name, int(slot))
            delayed_print("Game saved.\n", 0.5, 0)
            break

def prompt_save_forest_data(player):
    delayed_print("You have entered the city.", 3, 1)
    slot_name = input("Enter a name for your save slot: ")
    slot_input = input("Enter a slot number (or leave blank for next available): ")
    slot = int(slot_input) if slot_input.strip() else None
    save_forest_data(player, slot_name, slot)
    delayed_print("Your progress has been saved.", 3, 1)
def save_forest_data(player, slot_name, slot):
    data = {
        "forest_attributes": player.forest_attributes,
        "forest_items": player.forest_items,
        "forest_locations": player.last_forest_location,
        "visited_forest_locations": player.visited_forest_locations
    }
    data = serialize_functions_as_names(data)
    try:
        with open(saveFileName, "r") as f:
            json_data = json.load(f)
    except Exception as e:
        print("Error reading save file:", e)
        return
    if "slots" not in json_data:
        json_data["slots"] = {}
    if str(slot) not in json_data["slots"]:
        json_data["slots"][str(slot)] = {}
    # Overwrite slot with new save
    json_data["slots"][str(slot)] = {slot_name: data}
    try:
        with open(saveFileName, "w") as f:
            json.dump(json_data, f, indent=3)
    except Exception as e:
        print("Error writing to save file:", e)

def load_menu(player, city_path_func):
    slots = get_save_slots()
    if not slots:
        delayed_print("No saves to load.\n", 0.5, 0)
        return
    display_save_slots()
    delayed_print("\n", 0.5, 0)
    slot_input = input("Enter the slot number to load: ")
    slot = str(slot_input)
    if slot not in slots:
        delayed_print("Invalid slot.\n", 0.5, 0)
        return
    slot_names = list(slots[slot].keys())
    if len(slot_names) > 1:
        print("Multiple saves in this slot:")
        for idx, name in enumerate(slot_names):
            print(f"{idx+1}: {name}")
        name_idx = int(input("Choose save by number: ")) - 1
        slot_name = slot_names[name_idx]
    else:
        slot_name = slot_names[0]
    load_forest_data(player, slot, slot_name, city_path_func)
    delayed_print("Game loaded.\n", 0.5, 0)
def load_forest_data(player, slot, slot_name, city_path_func):
    try:
        if not os.path.exists(saveFileName):
            print(f"Error: Save file `{saveFileName}` does not exist.")
            return
        with open(saveFileName, "r") as f:
            try:
                json_data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error: Save file is corrupted or not valid JSON. Details: {e}")
                return
        slots = json_data.get("slots", {})
        if str(slot) not in slots:
            print(f"Error: Slot `{slot}` not found in save file.")
            return
        slot_data = slots[str(slot)].get(slot_name)
        if not slot_data:
            print(f"Error: Slot name `{slot_name}` not found in slot `{slot}`.")
            return
        # Check for required keys
        required_keys = ["forest_attributes", "forest_items", "forest_locations", "visited_forest_locations"]
        for key in required_keys:
            if key not in slot_data:
                print(f"Error: Key `{key}` missing in save data for slot `{slot}` and name `{slot_name}`.")
                return
        # Load data
        player.forest_attributes = slot_data.get("forest_attributes", {})
        player.forest_items = slot_data.get("forest_items", {})
        player.last_forest_location = slot_data.get("forest_locations", "")
        player.visited_forest_locations = slot_data.get("visited_forest_locations", {})
        player.update_path("city_path", city_path_func)
        print("Game loaded successfully.")
    except Exception as e:
        print(f"Unexpected error during load: {e}")

def serialize_functions_as_names(data):
    if isinstance(data, dict):
        return {k: serialize_functions_as_names(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [serialize_functions_as_names(v) for v in data]
    elif isinstance(data, types.FunctionType):
        return data.__name__
    else:
        return data
def get_save_slots():
    if not os.path.exists(saveFileName):
        return {}
    with open(saveFileName, "r") as f:
        data = json.load(f)
    return data.get("slots", {})
def display_save_slots():
    slots = get_save_slots()
    if not slots:
        print("No save slots available.")
        return
    print("Save Slots:")
    for slot_num, slot_data in slots.items():
        for name in slot_data:
            print(f"Slot {slot_num}: {name}")