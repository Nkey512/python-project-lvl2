import os
import json
import yaml


def get_path(path):
    path = os.path.expanduser(path)
    path = os.path.abspath(os.path.normpath(path))
    return path


def get_data(file_path):
    path = get_path(file_path)
    _, ext = os.path.splitext(path)
    if ext in {'.json'}:
        data = json.load(open(path))
    elif ext in {'.yml', '.yaml'}:
        data = yaml.safe_load(open(path))
    else:
        data = dict()
    return data
