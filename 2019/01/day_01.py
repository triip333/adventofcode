from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
'''

def part_1(input):
    return sum([int(l) // 3 - 2 for l in input.splitlines()])

def part_2(input):
    def total_fuel(amount):
        res = 0
        while amount > 0:
            a = amount // 3 - 2
            if a > 0:
                res += a
            amount = a
        return res
    return sum([total_fuel(int(l)) for l in input.splitlines()])

if __name__ == '__main__':
    input = get_input()
    print(part_1(input))
    print(part_2(input))
