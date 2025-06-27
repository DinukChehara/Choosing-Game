from Utils import get_valid_input, delayed_print

def city_path(player):
    save_slots = {}

    while True:
        choice = get_valid_input("Do you want to save or load your game? (save/load/exit)", ["save", "load", "exit"])
        if choice == "save":
            print("Available save slots:")
            for i, (slot_name, _) in enumerate(save_slots.items()):
                print(f"{i + 1}. {slot_name}")
            if len(save_slots) < 5:
                slot_name = get_valid_input("Enter a name for the save slot:")
                if slot_name in save_slots:
                    delayed_print("Save slot already exists!", 1, 0)
                    continue
                save_slots[slot_name] = player
                player.save_game(slot_name)
                delayed_print("Game saved!", 1, 0)
            else:
                delayed_print("No more save slots available!", 1, 0)
        elif choice == "load":
            print("Available save slots:")
            for i, (slot_name, _) in enumerate(save_slots.items()):
                print(f"{i + 1}. {slot_name}")
            slot_number = get_valid_input("Enter the number of the save slot to load (1-5):",
                                          list(range(1, len(save_slots) + 1)))
            slot_name = list(save_slots.keys())[slot_number - 1]
            player.load_game(slot_name)
        elif choice == "exit":
            break