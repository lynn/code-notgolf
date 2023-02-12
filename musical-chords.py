import sys

def semitone_value(note):
    letter = note[0]
    value = {'A': 0, 'B': 2, 'C': 3, 'D': 5, 'E': 7, 'F': 8, 'G': 10}[letter]
    if '♯' in note: value += 1
    if '♭' in note: value -= 1
    return value

for arg in sys.argv[1:]:
    chord = arg.split(' ')
    letters = {note[0] for note in chord}
    if letters == {'A', 'C', 'E'}: root_letter = 'A'
    if letters == {'B', 'D', 'F'}: root_letter = 'B'
    if letters == {'C', 'E', 'G'}: root_letter = 'C'
    if letters == {'D', 'F', 'A'}: root_letter = 'D'
    if letters == {'E', 'G', 'B'}: root_letter = 'E'
    if letters == {'F', 'A', 'C'}: root_letter = 'F'
    if letters == {'G', 'B', 'D'}: root_letter = 'G'
    root = [n for n in chord if n.startswith(root_letter)][0]
    
    intervals = {(semitone_value(note) - semitone_value(root)) % 12 for note in chord}
    if intervals == {0, 3, 6}: print(root + '°')
    if intervals == {0, 3, 7}: print(root + 'm')
    if intervals == {0, 4, 7}: print(root)
    if intervals == {0, 4, 8}: print(root + '+')
