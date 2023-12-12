from os import sys, path
import re, math
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
'''

def get_direction(directions_str):
    while True:
        res = [ch for ch in directions_str]
        while res:
            yield 1 if res.pop(0) == 'R' else 0


def part_1(directions_str, D):
    res = 0
    cur = 'AAA'
    directions = get_direction(directions_str)
    while cur != 'ZZZ':
        res += 1
        dir = next(directions)
        cur = D[cur][dir]
    return res


def part_2(directions_str, D):
    res = []
    for cur in [node for node in D.keys() if node[-1] == 'A']:
        i = 0
        directions = get_direction(directions_str)
        while cur[-1] != 'Z':
            i += 1
            dir = next(directions)
            cur = D[cur][dir]
        res.append(i)
    return math.lcm(*res)

if __name__ == '__main__':
    input = get_input()
    # input = sample
    input = input.split('\n\n')
    D = {}
    for line in input[1].splitlines():
        k, l, r = [m for m in re.findall('\w+', line)]
        D[k] = (l, r)

    print(part_1(input[0], D))
    print(part_2(input[0], D))
