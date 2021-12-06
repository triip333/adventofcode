from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

def part_1(input):
    res = 0
    for _ in input.split():
        l, w, h = map(int, _.split('x'))
        res += 2 * (l * w + l * h + w * h) + min(l * w, l * h, w * h)
    return res

def part_2(input):
    res = 0
    for _ in input.split():
        l, w, h = sorted(map(int, _.split('x')))
        res += 2 * l + 2 * w + l * w * h
    return res

if __name__ == '__main__':
    input  = get_input()
    print(part_1(input))
    print(part_2(input))
