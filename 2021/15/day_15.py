from os import sys, path
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms
from collections import defaultdict
import heapq

sample = '''\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581\
'''

def get_array(input, n):
    arr = []
    for i in range(n):
        for line in input.splitlines():
            arr.append([(int(ch) + i + j - 1) % 9 + 1 for j in range(n) for ch in line])
    return arr

@measure_ms
def solve(arr):
    def get_next(x, y):
        for i in [1, -1]:
            if (x + i, y) in unvisited:
                yield x + i, y
        for j in [1, -1]:
            if (x, y + j) in unvisited:
                yield x, y + j

    X, Y = len(arr[0]), len(arr)
    unvisited = {}

    for i in range(X):
        for j in range(Y):
            unvisited[(i, j)] = 1e9
    unvisited[(0, 0)] = 0
    h = [(0, (0, 0))]
    heapq.heapify(h)
    while h:
        cur_len, vertex = heapq.heappop(h)
        for x, y in get_next(vertex[0], vertex[1]):
            cur_len = unvisited[vertex] + arr[y][x]
            if cur_len < unvisited[(x, y)]:
                unvisited[(x, y)] = cur_len
                heapq.heappush(h, (cur_len, (x, y)))
        if vertex[0] == X - 1 and vertex[1] == Y - 1:
            return unvisited[vertex]
        unvisited.pop(vertex)

if __name__ == '__main__':
    input = get_input()
    # input = sample

    print(solve(get_array(input, 1)))
    print(solve(get_array(input, 5)))