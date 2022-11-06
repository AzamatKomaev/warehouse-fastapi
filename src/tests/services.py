import json


def get_data_from_file(directory: str, file_name: str) -> tuple:
    with open(f'{directory}/input_data/{file_name}', 'r') as f_input:
        input_data = json.load(f_input)

    with open(f'{directory}/output_data/{file_name}', 'r') as f_output:
        output_data = json.load(f_output)

    return input_data, output_data
