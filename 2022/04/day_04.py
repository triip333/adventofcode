from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''

def part_1(input):
    res = 0
    for line in input.splitlines():
        a, b = line.split(',')
        a1, a2 = [int(i) for i in a.split('-')]
        b1, b2 = [int(i) for i in b.split('-')]
        if (a1 <= b1 <= b2 <= a2) or (b1 <= a1 <= a2 <= b2):
            res += 1
            # print(a1, a2, b1, b2)
    return res

def part_2(input):
    res = 0
    for line in input.splitlines():
        a, b = line.split(',')
        a1, a2 = [int(i) for i in a.split('-')]
        b1, b2 = [int(i) for i in b.split('-')]
        if (a1 <= b1 <= a2) or (a1 <= b2 <= a2) or (b1 <= a1 <= b2) or (b1 <= a2 <= b2):
            res += 1
            print(a1, a2, b1, b2)
    return res

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))      
