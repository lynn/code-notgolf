import sys

# evenly(102, 5) == [21, 21, 20, 20, 20]
def evenly(n, bins):
    return [n // bins + (k < n % bins) for k in range(bins)]

# justify('May the Force be with you!', 33) == 'May   the   Force  be  with  you!'
def justify(line, W):
    gaps = line.count(' ')
    letters = len(line) - gaps
    spaces_to_distribute = W - letters
    space_counts = evenly(spaces_to_distribute, gaps)
    return ''.join(' ' * space_counts.pop(0) if c == ' ' else c for c in line)

def crawl(paragraphs, I, W):
    counter = 0
    lines = []
    def emit(line):
        nonlocal counter, I, W
        print(' ' * I + line)
        if counter % 2: I -= 1; W += 2
        counter += 1

    for p in paragraphs:
        while len(p) > W:
            i = p[:W+1].rindex(' ')
            emit(justify(p[:i], W))
            p = p[i+1:]
        emit(p)
        emit('')

for arg in sys.argv[1:]:
    header, *paragraphs = arg.split('\n')
    I, W = map(int, header.split())
    crawl(paragraphs, I, W)
