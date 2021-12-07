from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
from statistics import median

sample = '''\
16,1,2,0,4,2,7,1,2,14\
'''

def part_1():
    m = int(median(l))
    return sum(abs(m - i) for i in l)

def part_2():
    res = []
    for i in range(min(l), max(l) + 1):
        fuel = 0
        for j in l:
            move = abs(i - j)
            fuel += int(move * (move + 1) / 2)  
        res.append(fuel)
    return min(res)

if __name__ == '__main__':
    input = get_input()
    global l
    # l = [int(i) for i in sample.split(',')]
    l = [int(i) for i in input.split(',')]
    print(part_1())
    print(part_2())
