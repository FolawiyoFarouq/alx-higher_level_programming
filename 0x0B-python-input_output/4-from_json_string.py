#!/usr/bin/python3
"""Component 4-from_json_string.
Remits an item (Python data structure)
represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """Remits the item representing the my_str.
    Args:
        - my_str: JSON string representation
    Returns: corresponding object
    """

    return json.loads(my_str)
