
"""
exploring random methods

"""

import string
import random


# 2020-03-11 randomize string order, default string is alphabet
def shufflestring(input_string=string.ascii_lowercase):
    a = list(input_string) # convert string to list
    random.shuffle(a) # shuffle order of list items in place
    return str().join(a) # convert list back to string


# 2020-10-28 examine random distribution and boundaries
def freq_anal(given_list):
    result = {}
    for item in given_list:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result

def randrange_ints(a,b,c):
    return [random.randrange(a, b) for i in range(c)]

def randint_ints(a,b,c):
    return [random.randint(a, b) for i in range(c)]

def test_suite():
    start = 1
    stopp = 3
    count = 8192

    print('start', start, ', stop', stopp)

    the_list = randrange_ints(start, stopp, count)
    print('randrange', freq_anal(the_list))
    print('randrange', sorted(freq_anal(the_list).keys()))

    the_list = randint_ints(start, stopp, count)
    print('randint  ', freq_anal(the_list))
    print('randint  ', sorted(freq_anal(the_list).keys()))
