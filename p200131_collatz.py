"""
2020-01-31 Generate the Collatz sequence.

Exercise from "Automate the Boring Stuff", chapter 3.
A
Write a function named collatz_next() that has one parameter named number.
If even, print and return number // 2.
If oddd, print and return 3 * number + 1.
B
Write a program that takes user input as starting value,
then calls collatz_next() on that number until the function returns 1.
C
use try/except to catch non-integer user input
and print an appropriate error message
Hints
strings must be converted to ints before using math
number % 2 == 0 ==> even, number % 2 == 1 ==> odd

both collatz_next() and collatz_seq() must include input checks
what to test and when and how
    number is not int
        number is invalid
    number is < 1
        error
        number is invalid
    number is = 1
        maybe error
        this is the end of the seq, do not calc another number
    number is > 1
        not error
        calc next number
"""

def collatz_next(number):
    """Calculate the next number in the Collatz sequence."""
    try:
        if not isinstance(number, int):
            raise TypeError("Input not an int", number)
        if number < 1:
            raise ValueError("Input out of bounds", number)
        if number == 1:
            raise ValueError("End of sequence", number)
        number = int(number)
    except TypeError as err:
        return("TypeError", err.args)
    except ValueError as err:
        return("ValueError", err.args)
    else:
        if number % 2 == 0:
            next_number = number // 2
        else:
            next_number = number * 3 + 1
        return next_number

def collatz_seq(number):
    """Generate a complete Collatz sequence given an inital number."""
    try:
        if not isinstance(number, int):
            raise TypeError("Input not an int", number)
        if number < 1:
            raise ValueError("Input out of bounds", number)
        number = int(number)
    except TypeError as err:
        return("TypeError", err.args)
    except ValueError as err:
        return("ValueError", err.args)
    else:
        seq = []
        seq.append(number)
        while seq[-1] != 1:
            seq.append(collatz_next(seq[-1]))
        return seq
