from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
from itertools import combinations

sample = '''\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''

def solve(input, num):
    arr = [[ch for ch in line] for line in input.splitlines()]
    galaxies = set()
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == '#':
                galaxies.add((r, c))
    empty_r = set()
    for r in range(len(arr)):
        if len(arr[r]) == arr[r].count('.'):
            empty_r.add(r)
    empty_c = set()
    for c in range(len(arr[0])):
        if len(arr) == [arr[i][c] for i in range(len(arr[0]))].count('.'):
            empty_c.add(c)

    res = []
    for i, k in enumerate(combinations(galaxies, 2)):
        a, b = k
        dist, expanding = 0, 0
        for r in range(min(a[0], b[0]), max(a[0], b[0])):
            if r in empty_r:
                expanding += 1
            else:
                dist += 1
        for c in range(min(a[1], b[1]), max(a[1], b[1])):
            if c in empty_c:
                expanding += 1
            else:
                dist += 1
        res.append([dist, expanding])

    for i, item in enumerate(res):
        res[i] = [item[0], num * item[1]]
    return sum([item[0] + item[1] for item in res])

if __name__ == '__main__':
    input = get_input()
    # input = sample.rstrip()
    print(solve(input, 2))
    print(solve(input, 1000000))
