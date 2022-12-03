import pathlib
from adapters.file_adapter import config, get_txt_content, get_input_file_path

def max_elves_calories():
    input_file_content = get_txt_content(get_input_file_path('DAY_1'))
    max_calories = 0
    calories_counter = 0
    for line in input_file_content: 
        parsed_line = line.rstrip('\n')
        if  parsed_line == '':
            max_calories = calories_counter if calories_counter > max_calories else max_calories
            calories_counter = 0
        else: 
            calories_counter += int(parsed_line) 

    return max_calories

