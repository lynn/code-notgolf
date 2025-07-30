import sys

for arg in sys.argv[1:]:
    arg = arg.translate(str.maketrans('⑤⑥⑦⑧F-', '567800'))
    score = pins = roll = 0
    mult = [1] * 21
    for i, ch in enumerate(arg):
        if ch == ' ':
            continue
        frame = i // 3 + 1
        if ch == '/':
            pins = 10 - pins
            if frame <= 9:
                # If they get a spare in one of the first nine frames,
                # the value of the following roll is added as a bonus. 
                mult[roll + 1] += 1
        elif ch == 'X':
            pins = 10
            if frame <= 9:
                # If they get a strike in one of the first nine frames,
                # the value of the following two rolls, which may cover
                # multiple frames, is added as a bonus. 
                mult[roll + 1] += 1
                mult[roll + 2] += 1
        else:
            pins = int(ch)
        score += pins * mult[roll]
        roll += 1

    print(score)
