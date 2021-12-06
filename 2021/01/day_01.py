from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

def part_1(input):
    prev = None
    res = 0
    # print(input.split())
    for i in [int(i) for i in input.split()]:
        if prev and (prev < i):
            res += 1
        prev = i
    return res

def part_2(input):
    a, b, c = None, None, None
    res = 0
    for i in [int(i) for i in input.split()]:
        if a and b and c and (a + b + c < b + c + i):
            res += 1
        a = b
        b = c
        c = i
        prev = i
    return res

if __name__ == '__main__':
    input  = get_input()
    print(part_1(input))
    print(part_2(input))