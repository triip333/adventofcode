from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

def part_1(input):
    return input.count('(') - input.count(')')

def part_2(input):
    res = 0
    for i, ch in enumerate(input):
        if ch == '(':
            res += 1
        elif  ch == ')':
            res -= 1
        if res < 0:
            return i + 1

if __name__ == '__main__':
    input = get_input()
    print(part_1(input))
    print(part_2(input))