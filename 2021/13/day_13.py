from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5\
'''
arr = []

def debug():
    for a in arr:
        print(''.join(['#' if i > 0 else ' ' for i in a]))
    print()

def solve(input):
    global arr
    dots, fold = input.split('\n\n')
    max_x = max([int(line.split(',')[0]) for line in dots.split()])
    max_y = max([int(line.split(',')[1]) for line in dots.split()])
    for x in range(max_y + 1):
        arr.append([0 for x in range(max_x + 1)])
    for line in dots.split():
        x, y = map(int, line.split(','))
        arr[y][x] = 1

    res = 0
    for line in fold.split('\n'):
        line = line.replace('fold along ', '')
        d, l = line.split('=')
        l = int(l)
        if d == 'x':
            for x in range(len(arr[0]) - l - 1):
                for y in range(len(arr)):
                    if arr[y][l + x + 1] == 1:
                        arr[y][l - x - 1] = 1
            for y in range(len(arr)):
                arr[y] = arr[y][:l]
        if d == 'y':
            for y in range(len(arr) - l - 1):
                for x in range(len(arr[y])):
                    if arr[l + y + 1][x] == 1:
                        arr[l - y - 1][x] = 1
            arr = arr[:l]

        if res == 0:
            for y in range(len(arr)):
                res += sum(arr[y][x] for x in range(len(arr[y])))
    print(res)
    debug()

def part_2(input):
    return None

if __name__ == '__main__':
    input = get_input()
    # input = sample
    solve(input)
