'''
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

'''

import sys
import os.path

def parse():
    try:
        if not len(sys.argv) == 3:
            raise ValueError('Usage: bincop inputfile outputfile')
        if not os.path.exists(sys.argv[1]):
            raise ValueError('Input file does not exist: ', sys.argv[1])
        if os.path.exists(sys.argv[2]):
            raise ValueError('Output file already exists: ', sys.argv[2])
    except ValueError as err:
        print(''.join(err.args))
    else:
        process()

def process():
    print('Ok')

parse()
