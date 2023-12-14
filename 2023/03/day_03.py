from os import sys, path
import time, re
from collections import defaultdict
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
import math

sample = '''\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

digits = [str(i) for i in range(10)]

def get_surrounding(arr, r, c, ln):
    asterisk = []
    def get_val(r, c):
        if 0 <= r < len(arr) and 0 <= c < len(arr[r]):
            if arr[r][c] == '*':
                asterisk.append((r, c))
            return arr[r][c]

    res = []
    for dr in [-1, 1]:
        for dc in range(ln + 2):
            res.append(get_val(r + dr, c + dc - 1))
    res.append(get_val(r, c - 1))
    res.append(get_val(r, c + ln))

    return res, asterisk


def solve(input):
    res1, res2 = 0, 0
    d = defaultdict(list)
    arr = [[ch for ch in line] for line in input.splitlines()]
    for r, line in enumerate(input.splitlines()):
        c = 0
        numbers = [m for m in re.findall('\d+', line)]
        for num in numbers:
            c = line.index(num, c)
            surrounding, asterisk = get_surrounding(arr, r, c, len(num))
            if len(set(surrounding) - set(digits + ['.', None])) > 0:
                res1 += int(num)
            for a in asterisk:
                d[a].append(num)
            c += len(num)
    for _, v in d.items():
        if len(v) > 1:
            res2 += math.prod([int(i) for i in v])
    return res1, res2

if __name__ == '__main__':
    input = get_input()
    # input = sample.rstrip()
    print(solve(input))
