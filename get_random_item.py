"""
2020-01-28
Challenge: write a function that does this:
    Remove and return random item from the given list.
"""

from numpy.random import randint as npri

INPUT_LIST = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black']

def remove_and_return_random_item_from_list(given_list):
    """Remove and return random item from the given list."""
    return given_list.pop(npri(len(given_list)))

def shuffle_list(given_list):
    """Shuffle the given list."""
    out_list = []
    while given_list:
        out_list.append(remove_and_return_random_item_from_list(given_list))
    return out_list



#while INPUT_LIST:
#    print(remove_and_return_random_item_from_list(INPUT_LIST))
