import pathlib
from adapters.file_adapter import config, get_txt_content, get_input_file_path

def fill_calories_array(input_file_content):
    calories_array = []
    calories_counter = 0
    for line in input_file_content: 
        parsed_line = line.rstrip('\n')
        if  parsed_line == '':
            calories_array.append(calories_counter)
            calories_counter = 0
        else: 
            calories_counter += int(parsed_line) 
    return calories_array

def get_top_three_total(array): 
    array.sort(reverse=True)
    return array[0] + array[1] + array[2]

def get_top_three_elves_calories():
    input_file_content = get_txt_content(get_input_file_path('DAY_1'))
    calories_array = fill_calories_array(input_file_content)
    return get_top_three_total(calories_array)

