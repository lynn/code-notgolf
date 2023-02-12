import sys

# Replace hyphens neighboring digits with `digit`:
#
#        '0123--'              '01234-'
#  step( '1##---' , '4' )  ==  '1##4--'
#        '23----'              '234---'
#
def step(grid, digit):
    for y in range(9):
        row = ''
        for x in range(9):
            ch = grid[y][x]
            if ch == '-':
                if y > 0 and grid[y-1][x] >= '0': ch = digit
                if y < 8 and grid[y+1][x] >= '0': ch = digit
                if x > 0 and grid[y][x-1] >= '0': ch = digit
                if x < 8 and grid[y][x+1] >= '0': ch = digit
            row += ch
        yield row

    
for arg in sys.argv[1:]:
    grid = arg.split('\n')
    for digit in '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        grid = [*step(grid, digit)]
    print('\n'.join(grid) + '\n')
