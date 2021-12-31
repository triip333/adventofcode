from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
target area: x=20..30, y=-10..-5\
'''

def step(x_velocity, y_velocity):
    global x1, x2, y1, y2
    x, y = 0, 0
    max_y = 0
    while (x <= x2) and (y >= y1):
        x += x_velocity
        y += y_velocity
        max_y = max(max_y, y)
        if x1 <= x <= x2 and y1 <= y <= y2:
            return max_y
        if x_velocity > 0:
           x_velocity -= 1
        y_velocity -= 1


def part_1(input):
    res = []
    for x in range(1000):
        for y in range(1000):
            value = step(x, y)
            if value != None:
                res.append(value)
    return max(res)

def part_2(input):
    res = 0
    for x in range(1000):
        for y in range(-1000, 1000):
            value = step(x, y)
            if value != None:
                # print(value)
                res += 1
    return res

if __name__ == '__main__':
    input = get_input()
    # input = sample
    x, y = input.split(': ')[1].split(', ')
    x1, x2 = [int(i) for i in x.split('=')[1].split('..')]
    y1, y2 = [int(j) for j in y.split('=')[1].split('..')]
    print(part_1(input))
    print(part_2(input))      
