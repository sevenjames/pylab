"""
copy a file as a raw bytes object
2020-05-21
usage: bincop inputfile outputfile
"""

import sys
import os.path


def file_read(file):
    try:
        with open(file, mode='rb') as fob:
            return fob.read()
    except OSError as error:
        print(f'Read error: {error}')
        raise

def file_write(file, data):
    try:
        with open(file, mode='wb') as fob:
            fob.write(data)
    except OSError as error:
        print(f'Write error: {error}')
        raise

def check_args(args):
    try:
        if len(args) != 3:
            raise ValueError('Wrong number of arguments.')
        if not os.path.exists(args[1]):
            raise ValueError('Input file not found.')
        if os.path.exists(args[2]):
            raise ValueError('Output file already exists.')
    except ValueError as error:
        print(f'Error: {error}')
        print('Usage: bincop inputfile outputfile')
    else:
        return True

def main():
    """load entire file into bytes object, then write that object out"""
    if check_args(sys.argv):
        infile, outfile = sys.argv[1:3]
        print(f'Copying {infile} to {outfile}')
        data = file_read(infile)
        file_write(outfile, data)
        print('Copy success.')

if __name__ == "__main__":
    main()
