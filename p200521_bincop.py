"""
binary copy a file
2020-05-21

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

def check_args():
    if len(sys.argv) != 3:
        raise ValueError('Error: Wrong number of arguments.')
    if not os.path.exists(sys.argv[1]):
        raise ValueError('Error: Input file not found.')
    if os.path.exists(sys.argv[2]):
        raise ValueError('Error: Output file already exists.')

def process_file(inputfile, outputfile):
    print('Processing file...')
    with open(inputfile, mode='r', newline='') as file:
        print('foo')
        
def main():
    try:
        check_args()
    except ValueError as error:
        print(''.join(error.args))
        print('Usage: bincop inputfile outputfile')
    else:
        process_file(inputfile=sys.argv[1], outputfile=sys.argv[2])

if __name__ == "__main__":
    main()
