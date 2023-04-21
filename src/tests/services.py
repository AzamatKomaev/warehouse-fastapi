import json


def get_data_from_file(directory: str, file_name: str, return_output: bool = True) -> list[dict]:
    data_list = []

    with open(f'{directory}/input_data/{file_name}', 'r') as f_input:
        input_data = json.load(f_input)
        data_list.append(input_data)

    if return_output:
        with open(f'{directory}/output_data/{file_name}', 'r') as f_output:
            output_data = json.load(f_output)
            data_list.append(output_data)

    return data_list
