from os import sys, path
import time, re, random
from collections import defaultdict
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_s

sample = '''\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''

@measure_s
def part_1(input, line_number):
    positions = {}
    for line in input.strip().splitlines():
        sx, sy, bx, by = list(map(int, re.findall('-?\d+', line)))

        if sy == line_number:
            positions[sx] = 'S'
        elif by == line_number:
            positions[bx] = 'B'

        distance = abs(sx - bx) + abs(sy - by)
        for x in range(sx - distance + abs(sy - line_number), sx + distance - abs(sy - line_number) + 1):
            if x not in positions:
                positions[x] = '#'

    return len(list(filter(lambda x: positions[x] == '#', positions)))


@measure_s
def part_2(input, max_pos):

    lines = defaultdict(list)
    for line in input.strip().splitlines():
        sx, sy, bx, by = list(map(int, re.findall('-?\d+', line)))
    
        distance = abs(sx - bx) + abs(sy - by)
        for r in range(max(0, sy - distance), min(max_pos, sy + distance) + 1):
            lines[r].append((max(0, sx - distance + abs(sy - r)), min(max_pos, sx + distance - abs(sy - r))))

    for r in range(max_pos + 1):
        l = sorted(lines[r])
        x_from, x_to = l.pop(0)
        if x_from != 0:
            return 0, r
        while l:
            a, b = l.pop(0)
            if a > x_to + 1:
                return (x_to + 1, r)
            else:
                x_to = max(x_to, b)
        
if __name__ == '__main__':
    input = get_input()
    print(part_1(sample, 10))
    print(part_1(input, 2000000))
    print(part_2(sample, 20))
    res = part_2(input, 4000000)
    print(res)
    print(res[0] * 4000000 + res[1])