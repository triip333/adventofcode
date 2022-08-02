from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms


@measure_ms
def solve(arr, part_2):
    for _ in range(100):
        if part_2:
            arr[0][0] = '#'
            arr[0][99] = '#'
            arr[99][0] = '#'
            arr[99][99] = '#'
        new_arr = [['.' for _ in range(len(arr[0]))] for _ in range(len(arr))]
        for r in range(len(arr)):
            for c in range(len(arr[r])):
                count = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if i != 0 or j != 0:
                            if (0 <= r + i < len(arr)) and (0 <= c + j < len(arr[r])):
                                count += 1 if arr[r + i][c + j] == '#' else 0
                if arr[r][c] == '#' and count in [2, 3]:
                    new_arr[r][c] = '#'
                elif arr[r][c] == '.' and count == 3:
                    new_arr[r][c] = '#'
        arr = new_arr
    
    if part_2:
        arr[0][0] = '#'
        arr[0][99] = '#'
        arr[99][0] = '#'
        arr[99][99] = '#'
    res = 0
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == '#':
                res += 1
    return res

if __name__ == '__main__':
    input = get_input()

    arr = []
    for line in input.strip().split('\n'):
        arr.append([x for x in line])
    print(solve(arr, False))
    
    arr = []
    for line in input.strip().split('\n'):
        arr.append([x for x in line])
    print(solve(arr, True))