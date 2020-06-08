'''
2020-01-26
random int generation timing tests
https://stackoverflow.com/questions/4172131/create-random-list-of-integers-in-python

conclusion:
    random.randint is simply an alias to a form of random.randrange
    random.randrange is ok
    numpy.random.randint is faster by 2 orders of magnitude
'''

import timeit

t1 = timeit.Timer('[random.randint(0, 1000) for r in range(10000)]', 'import random')
t2 = timeit.Timer('[random.randrange(0, 999) for r in range(10000)]', 'import random')
t3 = timeit.Timer('nprand.randint(1000, size=10000)', 'import numpy.random as nprand')

print(t1.timeit(1000)/1000,'random.randint')
print(t2.timeit(1000)/1000,'random.randrange')
print(t3.timeit(1000)/1000,'nprand.randint')

