from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_s
from collections import defaultdict

sample = '''\
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
'''


class Elf():
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.next = None
    
    def __repr__(self):
        return f'({self.r}, {self.c})'
    
    def can_move(self, all_elves):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    if (self.r + dr, self.c + dc) in all_elves:
                        return True
        return False
    
    def check_position(self, all_elves, direction):
        for i in range(4):
            # N, NE, or NW
            if (direction + i) % 4 == 0:
                if not [True for dc in [-1, 0, 1] if (self.r - 1, self.c + dc) in all_elves]:
                    return (-1, 0)
            # S, SE, or SW
            if (direction + i) % 4 == 1:
                if not [True for dc in [-1, 0, 1] if (self.r + 1, self.c + dc) in all_elves]:
                    return (1, 0)
            # W, NW, or SW
            if (direction + i) % 4 == 2:
                if not [True for dr in [-1, 0, 1] if (self.r + dr, self.c - 1) in all_elves]:
                    return (0, -1)
            # E, NE, or SE
            if (direction + i) % 4 == 3:
                if not [True for dr in [-1, 0, 1] if (self.r + dr, self.c + 1) in all_elves]:
                    return (0, 1)

    def move(self):
        if self.next:
            self.r = self.next[0]
            self.c = self.next[1]
        self.next = None
    
    def clear(self):
        self.next = None


@measure_s
def solve(input):
    elves = []
    direction = 0
    global total_time
    for r, line in enumerate(input.splitlines()):
        for c, ch in enumerate(line):
            if ch == '#':
                elves.append(Elf(r, c))

    for round_count in range(int(1e6)):
        positions = set([(elf.r, elf.c) for elf in elves])
        for elf in elves:
            if elf.can_move(positions):
                _next = elf.check_position(positions, direction)
                if _next:
                    dr, dc = _next
                    elf.next = (elf.r + dr, elf.c + dc)

        d = defaultdict(int)
        for elf in elves:
            d[elf.next] += 1

        move_count = 0
        for elf in elves:
            if elf.next:
                move_count += 1
                if d[elf.next] == 1:
                    elf.move()
                else:
                    elf.clear()
        if move_count == 0:
            print(f'part 2: {round_count + 1}')
            return
        direction += 1
    
        if round_count == 9:
            r_min = min([elf.r for elf in elves])
            r_max = max([elf.r for elf in elves])
            c_min = min([elf.c for elf in elves])
            c_max = max([elf.c for elf in elves])
            print(f'part 1: {(r_max - r_min + 1) * (c_max - c_min + 1) - len(elves)}')

def part_2(input):
    return None

if __name__ == '__main__':
    input = get_input()
    # input = sample.strip()
    solve(input)