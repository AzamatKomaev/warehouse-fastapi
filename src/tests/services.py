import os
import json


def before_tests() -> None:
    if os.system('sh ./scripts/before.sh') != 0:
        raise ValueError('Could not run before.sh script.')


def after_tests() -> None:
    if os.system('sh ./scripts/after.sh') != 0:
        raise ValueError('Could not run after.sh script.')


def get_data_from_file(path: str) -> dict:
    with open(path, 'r') as f:
        json_data = json.load(f)
    return json_data
