from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms

@measure_ms
def part_1(input):
    arr = []
    for y in range(1000):
        arr.append([0 for x in range(1000)])

    for line in input.split('\n'):
        x1, y1 = map(int, line.split()[-3].split(','))
        x2, y2 = map(int, line.split()[-1].split(','))
        for x in range(x1, x2 + 1, 1):
            for y in range(y1, y2 + 1, 1):
                if line.startswith('turn on'):
                    arr[y][x] = 1
                elif line.startswith('turn off'):
                    arr[y][x] = 0
                elif line.startswith('toggle'):
                    arr[y][x] = (arr[y][x] + 1) % 2
    return sum(arr[y][x] for x in range(1000) for y in range(1000))

@measure_ms
def part_2(input):
    arr = []
    for y in range(1000):
        arr.append([0 for x in range(1000)])

    for line in input.split('\n'):
        x1, y1 = map(int, line.split()[-3].split(','))
        x2, y2 = map(int, line.split()[-1].split(','))
        for x in range(x1, x2 + 1, 1):
            for y in range(y1, y2 + 1, 1):
                if line.startswith('turn on'):
                    arr[y][x] += 1
                elif line.startswith('turn off'):
                    if arr[y][x] > 0:
                        arr[y][x] -= 1
                elif line.startswith('toggle'):
                    arr[y][x] += 2
    return sum(arr[y][x] for x in range(1000) for y in range(1000))

if __name__ == '__main__':
    input = get_input()
    print(part_1(input))
    print(part_2(input))      
