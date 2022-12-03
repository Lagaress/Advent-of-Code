import json

config_file_path = "/home/jesuslagares/Desktop/Advent-of-Code/config.json"

def get_config():
    with open(config_file_path, "r") as read_file:
        config = json.load(read_file)
    return config

config = get_config()

def get_txt_content(file_to_read): 
    with open(file_to_read, "r") as read_file:
        data = read_file.readlines()
    return data

def get_input_file_path(key): 
    return config['SOLUTIONS_FOLDER']+config['FOLDERS'][key]+config['INPUT']