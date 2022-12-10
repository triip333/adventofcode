from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''

C = {'noop': 1, 'addx': 2}

def part_1(input):
    res = 0
    cycle, X = 0, 1
    for line in input.splitlines():
        cmd = line.split()[0]
        for _ in range(C[cmd]):
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                res += cycle * X
                print(cycle, X, cycle * X, res)
            if cycle == 220:
                return res
        if cmd == 'addx':
            X += int(line.split()[1])

crt = {}
def part_2(input):
    res = 0
    cycle, X = 0, 1
    for line in input.splitlines():
        cmd = line.split()[0]
        for _ in range(C[cmd]):
            crt[cycle] = '#' if X - 1 <= ( cycle % 40 ) <= X + 1 else ' '
            cycle += 1
        if cmd == 'addx':
            X += int(line.split()[1])
    
    for r in range(6):
        line = ''
        for c in range(40):
            line += crt[r * 40 + c]
        print(line)
    

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))
