from os import sys, path
import re
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3\
'''

def test_sample(input, n):
    res = 0
    arr = []
    for line in input.strip().splitlines():
        arr.append([int(r) for r in re.findall('-?\d+', line)])
    for i0 in range(1, n):
        i1 = n - i0
        assert i0 + i1 == n
        score = 1
        for c in range(4):
            score *= max(0, i0 * arr[0][c] + i1 * arr[1][c])
        if score > res:
            print(i0, i1, score)
        res = max(res, score)
    return res

def part_1(input, n):
    res = 0
    arr = []
    for line in input.strip().splitlines():
        arr.append([int(r) for r in re.findall('-?\d+', line)])
    for i0 in range(1, n + 1):
        for i1 in range(1, n - i0 + 1):
            for i2 in range(1, n - i0 - i1 + 1):
                i3 = n - i0 - i1 - i2
                assert i0 + i1 + i2 + i3 == n
                score = 1
                for c in range(4):
                    score *= max(0, i0 * arr[0][c] + i1 * arr[1][c] + i2 * arr[2][c] + i3 * arr[3][c])
                res = max(res, score)
    return res

def part_2(input, n, target_calories):
    res = 0
    arr = []
    for line in input.strip().splitlines():
        arr.append([int(r) for r in re.findall('-?\d+', line)])
    for i0 in range(1, n + 1):
        for i1 in range(1, n - i0 + 1):
            for i2 in range(1, n - i0 - i1 + 1):
                i3 = n - i0 - i1 - i2
                assert i0 + i1 + i2 + i3 == n
                score = 1
                for c in range(4):
                    score *= max(0, i0 * arr[0][c] + i1 * arr[1][c] + i2 * arr[2][c] + i3 * arr[3][c])
                if target_calories == i0 * arr[0][4] + i1 * arr[1][4] + i2 * arr[2][4] + i3 * arr[3][4]:
                    res = max(res, score)
    return res

if __name__ == '__main__':
    input = get_input()
    print(test_sample(sample, 100))
    print(part_1(input, 100))
    print(part_2(input, 100, 500))
