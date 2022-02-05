"""
This module comprises functions for text editing
"""


def list_value_to_low_case(list_in):
    """
    Converts string, passed to a function in a list to a lowercase format

    Args:
        list_in: A list with strings

    Returns:
        A list with strings in lowercase
    """

    # list to be returned
    return_list = []

    # go through passed list and convert all characters to lowercase
    for entity in list_in:
        return_list.append(entity.lower())
    return return_list
