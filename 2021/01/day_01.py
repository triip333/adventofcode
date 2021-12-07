from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''
199
200
208
210
200
207
240
269
260
263\
'''

def part_1():
    return sum([1 if x < y else 0 for x, y in zip(l, l[1:])])

def part_2():
    # if x + (x + 1) + (x + 2) < (x + 1) + (x + 2) + (x + 3) ==> x < (x + 3)
    return sum([1 if x < y else 0 for x, y in zip(l, l[3:])])

if __name__ == '__main__':
    input = get_input()
    global l
    # l = [int(i) for i in sample.split()]
    l = [int(i) for i in input.split()]
    print(part_1())
    print(part_2())