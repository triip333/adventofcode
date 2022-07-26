from os import sys, path
from itertools import permutations
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141\
'''

def solve(input, fn):
    res = -1 * fn(-1, 1) * int(10e9)
    dist = {}
    citys = set()
    for line in input.strip().splitlines():
        line = line.split()
        a, b, d = line[0], line[2], int(line[4])
        dist[a, b] = d
        dist[b, a] = d
        citys.add(a)
        citys.add(b)
    for p in list(permutations(citys, len(citys))):
        d = 0
        for a, b in zip(p[:-1], p[1:]):
            d += dist[a, b]
        res = fn(res, d)
    return res

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(solve(input, min))
    print(solve(input, max))
