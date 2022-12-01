from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
'''

def part_1(input):
    res = []
    for calories in input.split('\n\n'):
        res.append(sum(int(i) for i in calories.splitlines()))
    return max(res)

def part_2(input):
    res = []
    for calories in input.split('\n\n'):
        res.append(sum(int(i) for i in calories.splitlines()))
    return sum(sorted(res)[-3:])

if __name__ == '__main__':
    input = get_input()
    print(part_1(input))
    print(part_2(input))
