from os import sys, path
from functools import cache
import re
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
20
15
10
5
5\
'''
res_set = set()

@cache
def load_combinations(amount, containers, combination=tuple()):
    global res_set
    
    for i in range(len(containers)):
        arr = list(containers)
        size = arr.pop(i)
        if amount - size[1] == 0:
            res_set.add(tuple(sorted(list(combination) + [size[0]])))
        elif amount - size[1] > 0:
            load_combinations(amount - size[1], tuple(arr), tuple(sorted(list(combination) + [size[0]])))

def solve(input, n):
    containers = [(i, int(x)) for i, x in enumerate(input.strip().splitlines())]
    load_combinations(n, tuple(containers))
    return len(res_set)

if __name__ == '__main__':
    input = get_input()
    # print(solve(sample, 25))
    print(solve(input, 150))
    m = min([len(x) for x in res_set])
    print(sum(1 for x in res_set if len(x) == m ))