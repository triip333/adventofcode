from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms
from functools import reduce

sample = '''\
2199943210
3987894921
9856789892
8767896789
9899965678\
'''

def get_adjacent(i, j):
    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if (x, y) in D and D[(x, y)] not in [-1, 9]:
            yield (x, y)

def part_1():
    res = 0
    for k, v in D.items():
        lowest = True
        for a in get_adjacent(k[0], k[1]):
            lowest = lowest and (v < D[a])
        if lowest:
            res += v + 1
    return res

def part_2():
    basin_sizes = []
    for k, v in D.items():
        if D[k] not in [-1, 9]:
            lst = [k]
            D[k] = -1
            for l in lst:
                for a in get_adjacent(l[0], l[1]):
                    D[a] = -1
                    lst.append(a)
            basin_sizes.append(len(lst))
    return reduce(lambda x, y: x * y, sorted(basin_sizes)[-3:])

if __name__ == '__main__':
    input = get_input()
    # input = sample
    D = {}
    for i, line in enumerate(input.split()):
        for j, ch in enumerate(line):
            D[(j, i)] = int(ch)

    print(part_1())
    print(part_2())
