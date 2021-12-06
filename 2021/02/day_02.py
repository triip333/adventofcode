from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

def part_1(input):
    res = 0
    f, d = 0, 0
    for _ in input.split('\n'):
        cmd, val = _.split()
        val = int(val)
        if cmd == 'forward':
            f += val
        elif cmd == 'down':
            d += val
        elif cmd == 'up':
            d -= val
    return f * d

def part_2(input):
    res = 0
    h_pos, depth, aim = 0, 0, 0
    for _ in input.split('\n'):
        cmd, val = _.strip().split()
        val = int(val)
        if cmd == 'forward':
            h_pos += val
            depth += val * aim
        elif cmd == 'down':
            aim += val
        elif cmd == 'up':
            aim -= val
    return h_pos * depth

if __name__ == '__main__':
    input  = get_input()
    print(part_1(input))
    ex = '''\
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
    '''
    # print(part_2(ex))
    print(part_2(input))