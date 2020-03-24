"""
2020-02-12
Character Picture Grid
Exercise from "Automate the Boring Stuff", chapter 4.
Given a list of lists of single character strings,
print the transposition of the list
hint: use a loop within a loop

"""

#print(col row)
#print(00 01 02 03 04 05 06 07 08)
#print(10 11 12 13 14 15 16 17 18)


GRID1 = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]

def print_grid(grid):
    """Print input array transposed."""
    cols = len(grid[0])
    rows = len(grid)

    for col in range(cols):
        for row in range(rows):
            print(grid[row][col], end='')
        print()

print_grid(GRID1)
