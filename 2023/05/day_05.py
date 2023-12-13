from os import sys, path
import re
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

def part_1(input):
    res = []
    almanac = [l.splitlines() for l in input.split('\n\n')]
    seeds = [int(m) for m in re.findall('\d+', almanac.pop(0)[0])]
    for seed in seeds:
        for a in almanac:
            for i in range(1, len(a)):
                dest_cat, src_cat, range_len = [int(num) for num in a[i].split()]
                if src_cat <= seed < src_cat + range_len:
                    seed = dest_cat + seed - src_cat
                    break
        res.append(seed)

    return min(res)

def part_2(input):
    almanac = [l.splitlines() for l in input.split('\n\n')]
    ranges = [int(m) for m in re.findall('\d+', almanac.pop(0)[0])]
    r = []
    while ranges:
        seed = ranges.pop(0)
        amount = ranges.pop(0)
        r.append((seed, seed + amount - 1))
    ranges = r

    for a in almanac:
        tmp = []
        while ranges:
            start, end = ranges.pop(0)
            for i in range(1, len(a)):
                dest_cat, src_cat, range_len = [int(num) for num in a[i].split()]
                delta = dest_cat - src_cat
                if src_cat <= start <= end < src_cat + range_len:
                    tmp.append((start + delta, end + delta))
                    start, end = None, None
                    break
                elif src_cat <= start < src_cat + range_len:
                    tmp.append((start + delta, src_cat + range_len - 1 + delta))
                    ranges.append((src_cat + range_len, end))
                    start, end = None, None
                    break
                elif src_cat <= end < src_cat + range_len:
                    tmp.append((src_cat + delta, end + delta))
                    ranges.append((start, src_cat - 1))
                    start, end = None, None
                    break
            if start and end:
                tmp.append((start, end))
        ranges = tmp

    return min([start for start, _ in ranges])

if __name__ == '__main__':
    input = get_input()
    # input = sample.rstrip()
    print(part_1(input))
    print(part_2(input))
