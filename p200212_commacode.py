"""
2020-02-12
Comma Code
Exercise from "Automate the Boring Stuff", chapter 4.
Write a function that takes a list and returns a string
composed of the list items separated by comma-space
and with an "and" inserted before the last item.
example
input = ['red', 'blue', 'green']
output: 'red, blue, and green'

"""

SAMPLE_LIST = ['dog', 'cat', 'fish', 'moose', 'tiger', 'bee']

def lst_to_str_1(the_list):
    """Return comma separated string of list items. With and.
    using the + concatenation operater
    """
    wlist = the_list[:] # makes a copy, not a new reference
    wlist[-1] = 'and ' + wlist[-1] # prepend last value with and
    the_str = ''
    for word in wlist:
        the_str += word + ', '
    the_str = the_str[:-2] # remove final comma space
    return the_str

def lst_to_str_2(the_list):
    """Return comma separated string of list items. With and.
    using the join method
    """
    wlist = the_list[:]
    wlist[-1] = ''.join(['and ', wlist[-1]])
    the_str = ', '.join(wlist)
    return the_str
