import json
import yaml


def parse_file(file_path):
    if file_path.endswith('.json'):
        file = json.load(open(file_path))
    else:
        file = yaml.safe_load(open(file_path))
    return file
