"""
2020-05-21
binary copy a file

bincop inputfile outputfile
    if args count is not 2, fail, print usage
    if inputfile doesn't exist, fail, print error
    if outputfile does exist, fail, print error
    load inputfile (in chunks?)
    write outputfile

consider
    sys.argv or argparse
    os.path.exists('./file')
    with open(mode='rb')

"""

import sys
import os.path

def parse():
    try:
        if not len(sys.argv) == 3:
            raise ValueError('Error: Wrong number of arguments.')
        if not os.path.exists(sys.argv[1]):
            raise ValueError('Error: Input file not found.')
        if os.path.exists(sys.argv[2]):
            raise ValueError('Error: Output file already exists.')
    except ValueError as err:
        print(''.join(err.args))
        print('Usage: bincop inputfile outputfile')
    else:
        process()

def process():
    print('Ok')

parse()
