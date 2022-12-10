from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample_1 = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''

sample_2 = '''\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
'''

directions = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}


def solve(input, n):
    rope = []
    for _ in range(n):
        rope.append([0, 0])
    positions = set()
    for line in input.splitlines():
        dir, amount = line[0], int(line.split()[1])
        for _ in range(amount):
            H = rope[0]
            H[0] = H[0] + directions[dir][0]
            H[1] = H[1] + directions[dir][1]
            for H, T in zip(rope, rope[1:]):
                if abs( T[0] - H[0] ) > 1 or abs( T[1] - H[1] ) > 1:
                    if T[0] != H[0]:
                        T[0] += 1 if T[0] < H[0] else -1
                    if T[1] != H[1]:
                        T[1] += 1 if T[1] < H[1] else -1
            positions.add((T[0], T[1]))
    return len(positions)


if __name__ == '__main__':
    input = get_input()
    assert solve(sample_1, 2) == 13
    print(solve(input, 2))
    assert solve(sample_2, 10) == 36
    print(solve(input, 10))