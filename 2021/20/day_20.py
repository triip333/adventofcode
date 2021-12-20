from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms

sample = '''\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###\
'''

def debug(D):
    min_x = min([k[0] for k in D.keys()])
    max_x = max([k[0] for k in D.keys()])
    min_y = min([k[1] for k in D.keys()])
    max_y = max([k[1] for k in D.keys()])
    for y in range(min_y, max_y + 1):
        s = ''
        for x in range(min_x, max_x + 1):
            s += '#' if D.get((x, y)) else '.'
        print(s)
    print()

@measure_ms
def solve(input, n):
    D = {}
    l = input.splitlines()
    algorithm = l.pop(0)
    l.pop(0)
    for y, line in enumerate(l):
        for x, ch in enumerate(line):
            if ch == '#':
                D[(x, y)] = True

    for step in range(n):
        N = {}
        min_x = min([k[0] for k in D.keys()])
        max_x = max([k[0] for k in D.keys()])
        min_y = min([k[1] for k in D.keys()])
        max_y = max([k[1] for k in D.keys()])

        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                b = ''
                for j in [-1, 0, 1]:
                    for i in [-1, 0, 1]:
                        if (min_x <= x + i <= max_x) and (min_y <= y + j <= max_y):
                            is_on = D.get((x + i, y + j))
                        else:
                            is_on = step % 2 and algorithm[0] == '#'
                        b += '1' if is_on else '0'
                if algorithm[int(b, 2)] == '#':
                    N[(x, y)] = True
        D = N
    return len(D)

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(solve(input, 2))
    print(solve(input, 50))
