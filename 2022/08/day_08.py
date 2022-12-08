from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
30373
25512
65332
33549
35390
'''

def part_1(input):
    visible = 0
    arr = []
    for line in input.splitlines():
        arr.append([int(i) for i in line])
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if r == 0 or r == len(arr) - 1 or c == 0 or c == len(arr[0]) - 1:
                visible += 1
            else:
                visible += 1 if (
                    all([arr[r][i] < arr[r][c] for i in range(c)])
                    or all([arr[r][i] < arr[r][c] for i in range(c + 1, len(arr[c]))])
                    or all([arr[i][c] < arr[r][c] for i in range(r)])
                    or all([arr[i][c] < arr[r][c] for i in range(r + 1, len(arr))])) else 0

    return visible

def part_2(input):
    best = 0
    arr = []
    for line in input.splitlines():
        arr.append([int(i) for i in line])
    for r in range(1, len(arr) - 1):
        for c in range(1, len(arr[0]) - 1):
            left, right, up, down = 0, 0, 0, 0
            for i in range(c - 1, -1, -1):
                left += 1
                if arr[r][c] <= arr[r][i]:
                    break
            for i in range(c + 1, len(arr[r])):
                right += 1
                if arr[r][c] <= arr[r][i]:
                    break
            for i in range(r - 1, -1, -1):
                up += 1
                if arr[r][c] <= arr[i][c]:
                    break
            for i in range(r + 1, len(arr)):
                down += 1
                if arr[r][c] <= arr[i][c]:
                    break
            best = max(best, left * right * up * down)
    return best

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))      
