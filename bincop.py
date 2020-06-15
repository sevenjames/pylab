"""
copy a file as a raw bytes object
2020-05-21
usage: bincop inputfile outputfile
"""

import sys

def main():
    """load entire file into bytes object, then write that object out.
    open mode rb : read bytes, fails if file not found
    open mode xb : write bytes, exclusive create, fail if file is found
    """
    try:
        if len(sys.argv) != 3:
            raise ValueError('Wrong number of arguments.')
    except ValueError as error:
        print(f'Error: {error}')
        print('Usage: bincop.py <inputfile> <outputfile>')
    else:
        print(f'Copying {sys.argv[1]} to {sys.argv[2]}')
        try:
            with open(sys.argv[1], mode='rb') as fob:
                data = fob.read()
        except OSError as error:
            print(f'File error: {error}')
        else:
            # process(data) goes here
            try:
                with open(sys.argv[2], mode='xb') as fob:
                    fob.write(data)
            except OSError as error:
                print(f'File error: {error}')
            else:
                print('ok')

if __name__ == "__main__":
    main()
    # args_thing()
