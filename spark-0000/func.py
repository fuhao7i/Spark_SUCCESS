import json


def json_to_dict(filename):
    json_file = open(filename, 'r', encoding='utf-8')
    return json.loads(json_file.read())