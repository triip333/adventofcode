from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms

sample = '''\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''

def part_1(input):
    res = set()
    arr = []
    for line in input.splitlines():
        arr.append([ch for ch in line])
    for r in range(len(arr)):
        if 'S' in arr[r]:
            c = arr[r].index('S')
            arr[r][c] = 'a'
            break

    visited = [(r, c)]
    queue = [(r, c, 0)]
    while queue:
        r, c, cost = queue.pop(0)
        for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dr = r + delta[0]
            dc = c + delta[1]
            if 0 <= dr < len(arr) and 0 <= dc < len(arr[dr]):
                if arr[r][c] == 'z' and arr[dr][dc] == 'E':
                    res.add(cost + 1)
                elif not (dr, dc) in visited and (ord(arr[dr][dc]) - ord(arr[r][c]) <= 1):
                    visited.append((dr, dc))
                    queue.append((dr, dc, cost + 1))

    return min(res)


def part_2(input):
    res = set()
    arr = []
    for line in input.splitlines():
        arr.append([ch for ch in line])
    for r in range(len(arr)):
        if 'E' in arr[r]:
            c = arr[r].index('E')
            arr[r][c] = 'z'
            break

    visited = [(r, c)]
    queue = [(r, c, 0)]
    while queue:
        r, c, cost = queue.pop(0)
        for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dr = r + delta[0]
            dc = c + delta[1]
            if 0 <= dr < len(arr) and 0 <= dc < len(arr[dr]):
                if arr[r][c] == 'b' and arr[dr][dc] in ['a', 'S']:
                    res.add(cost + 1)
                elif not (dr, dc) in visited and (ord(arr[r][c]) - ord(arr[dr][dc]) <= 1):
                    visited.append((dr, dc))
                    queue.append((dr, dc, cost + 1))

    return min(res)


if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))