from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
    
sample = '''\
1
2
-3
3
-2
0
4
'''

def solve(input, num, key):
    initial = [(pos, val * key) for pos, val in enumerate(map(int, input.strip().splitlines()))]
    zero = [(i, val) for i, val in initial if val == 0][0]
    l = initial[:]

    for _ in range(num):
        for i, val in initial:
            cur_pos = l.index((i, val))
            l.pop(cur_pos)
            new_pos = (cur_pos + val) % len(l)
            l.insert(new_pos, (i, val))
    
    return sum([l[(l.index(zero) + i * 1000) % len(l)][1] for i in range(1, 4)])

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(solve(input, 1, 1))
    print(solve(input, 10, 811589153))