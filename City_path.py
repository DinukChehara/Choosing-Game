from Player import prompt_save_forest_data

from Utils import delayed_print, get_valid_input, error_check

def city_path(player):
    prompt_save_forest_data(player)
    error_check(player)