from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms
from collections import defaultdict
from functools import cache

sample = '''\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C\
'''

@measure_ms
def part_1():
    t = template
    for i in range(10):
        new_t = [t[0]]
        for a, b in zip(t, t[1:]):
            if a + b in D:
                new_t.append(D[a + b])
            new_t.append(b)
        t = new_t
    return max([t.count(a) for a in set(t)]) - min([t.count(a) for a in set(t)])

@measure_ms
def part_2():
    def get_half(a, b):
        t = [a, b]
        for _ in range(20):
            new_t = [t[0]]
            for a, b in zip(t, t[1:]):
                new_t.append(D[a + b])
                new_t.append(b)
            t = new_t
        return t

    @cache
    def get_res(a, b):
        R = {}
        res = get_half(a, b)
        for r in set(res):
            R[r] = res.count(r)
        R[res[-1]] -= 1
        return R

    C = defaultdict(int)
    C[template[-1]] = 1
    for a1, b1 in zip(template, template[1:]):
        r1 = get_half(a1, b1)
        for a2, b2 in zip(r1, r1[1:]):
            for k, v in get_res(a2, b2).items():
                C[k] += v
    return max(C.values()) - min(C.values())

if __name__ == '__main__':
    input = get_input()
    # input = sample
    D = {}
    template, input = [line for line in input.split('\n\n')]
    for line in input.split('\n'):
        a, _, b = line.split()
        D[a] = b
    print(part_1())
    print(part_2())