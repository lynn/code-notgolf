from collections import defaultdict
import sys

for arg in sys.argv[1:]:
    arg = arg.translate(str.maketrans('⑤⑥⑦⑧F-', '567800'))
    score = pins = roll = 0
    bonus = defaultdict(int)
    for i, ch in enumerate(arg):
        if ch == ' ':
            continue
        roll += 1
        frame = i // 3 + 1
        if ch == '/':
            pins = 10 - pins
            if frame <= 9:
                bonus[roll + 1] += 1
        elif ch == 'X':
            pins = 10
            if frame <= 9:
                bonus[roll + 1] += 1
                bonus[roll + 2] += 1
        else:
            pins = int(ch)
        score += pins * (1 + bonus[roll])

    print(score)
