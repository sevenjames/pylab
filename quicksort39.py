'''
2020-01-24
programming challenge from SciPy Lecture Notes
section 1.2.4 Getting Started > The Python Language > Functions
https://scipy-lectures.org/intro/language/functions.html
Implement the quicksort algorithm, as defined by wikipedia
'''

import random

def quicksort(the_list):
    ''' sort the given list using the quicksort algorithm
    return a sorted list
    '''
    if len(the_list) < 2: # dont try to sort a list of 1 item
        return the_list
    lower = []
    upper = []
    pivot = the_list[0] # select first item as the pivot
    other = the_list[1:]
    for test_item in other: # separate the list based on pivot
        if test_item <= pivot:
            lower.append(test_item)
        else:
            upper.append(test_item)
    # run this function recursively on each sub-list
    # concatenate each sorted sublist into final sorted list
    return quicksort(lower) + [pivot] + quicksort(upper)

def test_sort():
    ''' test the quicksort function '''
    int_range, int_count = 99, 12
    random_integers = [random.randrange(int_range) for i in range(int_count)]
    sorted_random_integers = quicksort(random_integers)
    print("random integers:", random_integers)
    print("sorted integers:", sorted_random_integers)

test_sort()
