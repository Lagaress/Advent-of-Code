import pathlib
from adapters.file_adapter import config, get_txt_content, get_input_file_path

plays_score = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

def get_total_strategy_score():
    input_file_content = get_txt_content(get_input_file_path('DAY_2'))
    total_points = 0
    for line in input_file_content: 
        parsed_line = line.rstrip('\n')
        total_points += plays_score[parsed_line]
    return total_points
