import sys

qr = sys.argv[1].split('\n')

def read_bit(x, y):
    value = qr[y][x] == '#'
    mask = (x + y) % 2 == 0
    return '01'[value ^ mask]

bits = ''

# "The [...] vertical 'strips' of ^^ or vv must be read from right to left."
# "The bits in a strip are stored in a zig-zag order: ^^ zig-zags upwards, and vv zig-zags downwards."
for strip in range(6):
    x = 19 - 2 * strip
    for pos in range(21):
        y = 20 - pos if strip % 2 == 0 else pos

        # Skip over the "finder pattern" (top-right corner) and "timing pattern" (row y==6).
        if (x < 13 or y > 8) and y != 6:
            bits += read_bit(x + 1, y)
            bits += read_bit(x, y)

for i in range(17):
    byte = int(bits[8 * i + 12:8 * i + 20], 2)
    print(end=chr(byte))
