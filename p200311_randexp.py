
"""
2020-03-11
random experiments

"""

import string
import random

def shufflebet():
    a = list(string.ascii_lowercase)
    random.shuffle(a)
    return str().join(a)
