#!/usr/bin/python3
"""Component 6-load_from_json_file.
Generate an Article from a “JSON file”.
"""


import json


def load_from_json_file(filename):
    """Generate an item from title.
    Args:
        - title: name of the JSON file
    Remits: the article
    """

    with open(filename, 'r') as f:
        return json.load(f)
