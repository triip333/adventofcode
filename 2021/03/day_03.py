from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010\
'''

def part_1(input):
    lst = input.split()
    ln = len(lst[0])
    gamma = ''
    epsilon = ''
    for i in range(ln):
        bit_cnt = 0
        for item in lst:
            bit_cnt += int(item[i])
        gamma += str(round(bit_cnt/len(lst)))
        epsilon  += str((round(bit_cnt/len(lst)) + 1) % 2)
    return int(gamma, 2) * int(epsilon, 2)

def part_2(input):
    lst = input.split()
    l1, l2 = lst[:], lst[:]
    ln = len(lst[0])
    for i in range(ln):
        bit_cnt = 0
        _l1 = []
        for item in l1:
            bit_cnt += int(item[i])
        bit = '1' if bit_cnt >= len(l1) / 2 else '0'
        for item in l1:
            if item[i] == bit:
                _l1.append(item)
        l1 = _l1
        if len(l1) == 1:
            break

    for i in range(ln):
        bit_cnt = 0
        _l2 = []
        for item in l2:
            bit_cnt += int(item[i])
        bit = '1' if bit_cnt < len(l2) / 2 else '0'
        for item in l2:
            if item[i] == bit:
                _l2.append(item)
        l2 = _l2
        if len(l2) == 1:
            break

    return int(l1[0], 2) * ( int(l2[0], 2))

if __name__ == '__main__':
    input = get_input()
    print(part_1(input))
    print(part_2(input))
