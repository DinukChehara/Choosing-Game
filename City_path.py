from Player import prompt_save_forest_data
from Utils import delayed_print, get_valid_input, check

def city_path(player):
    delayed_print("You have entered the city.", 1)
    # Save the player's forest data upon entering the city
    prompt_save_forest_data(player)
    delayed_print("Your progress has been saved.", 1)