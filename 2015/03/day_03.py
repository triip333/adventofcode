from os import sys, path
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
from collections import defaultdict

def get_pos(input):
    x, y = 0, 0
    yield(x, y)
    for ch in input:
        if ch == '^':
            x += 1
        elif ch == 'v':
            x -= 1
        elif ch == '>':
            y += 1
        elif ch == '<':
            y -= 1
        yield(x, y)

def part_1(input):
    D = defaultdict(int)
    for x, y in get_pos(input):
        D[(x, y)] += 1
    return len(D)

def part_2(input):
    D = defaultdict(int)
    for x, y in get_pos(''.join([input[2 * i] for i in range(len(input) // 2)])):
        D[(x, y)] += 1
    for x, y in get_pos(''.join([input[2 * i + 1] for i in range(len(input) // 2)])):
        D[(x, y)] += 1
    return len(D)

if __name__ == '__main__':
    input = get_input()
    print(part_1(input))
    print(part_2(input))      
