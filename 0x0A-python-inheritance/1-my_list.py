#!/usr/bin/python3
"""1-my_list module
"""


class MyList(list):
    """_A class that takes over from list
    Args:
        list (_type_): _description_
    """
    def print_sorted(self):
        """Prints the grouped list
        """
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
