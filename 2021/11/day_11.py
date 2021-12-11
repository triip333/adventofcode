from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526\
'''

LEN = 10

def parse(input):
    global arr
    arr = [[0 for _ in range(LEN)] for _ in range(LEN)]
    for i, line in enumerate(input.split()):
        for j, l in enumerate(line):
            arr[i][j] = int(l)

def get_adjacent(i, j):
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if ((x != 0) or (y != 0)) and (0 <= i + x < LEN) and (0 <= j + y < LEN):
                yield i + x, j + y

def step():
    for i in range(LEN):
        for j in range(LEN):
            arr[i][j] += 1
    done = []
    flashed = True
    flash_count = 0
    while flashed:
        flashed = False
        for i in range(LEN):
            for j in range(LEN):
                if ( arr[i][j] > 9 ) and  ((i, j) not in done):
                    flashed = True
                    flash_count += 1
                    done.append((i, j))
                    for x, y in get_adjacent(i, j):
                        arr[x][y] += 1
    for i in range(LEN):
        for j in range(LEN):
            if arr[i][j] > 9:
                arr[i][j] = 0
    return flash_count

def part_1(input):
    res = 0
    parse(input)
    for i in range(100):
        res += step()
    return res

def part_2(input):
    parse(input)
    for i in range(int(1e6)):
        if step() == 100:
            return i + 1

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))      
