from os import sys, path
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

def get_combinations(amount, containers, combination=[]):
    global res_set
    res = 0
    
    for i in range(len(containers)):
        arr = containers[:]
        size = arr.pop(i)
        if amount - size[1] == 0:
            # combination.append(size)
            res_set.add(tuple(sorted(combination + [size])))
            print(combination)
            res += 1
        elif amount - size[1] > 0:
            res += get_combinations(amount - size[1], arr, combination + [size])

    return len(res_set)

def part_1(input, n):
    containers = [(i, int(x)) for i, x in enumerate(input.strip().splitlines())]
    return get_combinations(n, containers)
    

def part_2(input):
    pass

if __name__ == '__main__':
    input = get_input()
    print(part_1(sample, 25))
    print(part_1(input, 100))
    print(part_2(input))
    for i in res_set:
        print(i)
