from os import sys, path
import time, re
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5\
'''

sample = '''\
        ...#....
        .#......
        #.......
        ........
...#.......#....
........#.......
..#....#........
..........#.....
        ...#....
        .....#..
        .#......
        ......#.

10R3R10\
'''

right = 0
down = 1
left = 2
up = 3

move_ch = {right: '>', down: 'v', left: '<', up: '^'}
max_r, max_c, cube_size = 0, 0, 0
map = {}
cube_map = {}

def draw(cur_r, cur_c):
    with open('debug.txt', 'a') as f:
        for r in range(max_r + 1):
            line = ''
            for c in range(max_c + 1):
                if r == cur_r and c == cur_c:
                    line += 'O'
                else:
                    line += map[r, c] if (r, c) in map else ' '
            print(line)
            # f.write(line + '\n')
        print()
        # f.write('\n')

def get_next_pos_part_1(r, c, dir):
    delta = {right: (0, 1), down: (1, 0), left: (0, -1), up: (-1, 0)}
    dr, dc = delta[dir]
    for i in range(1, max(max_r, max_c)):
        new_r, new_c = (r + i * dr) % (max_r + 1), (c + i * dc) % (max_c + 1)
        if (new_r, new_c) in map:
            return new_r, new_c

def get_next_pos_part_2(r, c, dir):
    pass

def part_1(input, next_pos):
    r, c, dir = 0, min([c for r, c in map.keys() if r == 0]), right

    for move in re.findall('(\d+|R|L)', path):
        # with open('debug.txt', 'a') as f:
        print(f'{move} ({r}, {c}), {move_ch[dir]}')
            # f.write(f'{move} ({r}, {c}), {move_ch[dir]}\n')
        if move.isnumeric():
            for _ in range(int(move)):
                new_r, new_c = next_pos(r, c, dir)
                if map[(new_r, new_c)] != '#':
                    map[(r, c)] = move_ch[dir]
                    r, c = new_r, new_c
                else:
                    break
        else:
            dir = (dir + (1 if move == 'R' else -1)) % 4
        # draw(r, c)

    return 1000 * (r + 1) + 4 * (c + 1) + dir


def part_2(input):
    return None

if __name__ == '__main__':
    input = get_input()
    input = sample

    l = [line for line in input.split('\n')]
    path = l.pop()
    for r, line in enumerate(l):
        for c, ch in enumerate(line):
            if ch != ' ':
                map[(r, c)] = ch
                max_r = max(max_r, r)
                max_c = max(max_c, c)
    cube_size = max_r // 3

#         1111
#         1111
#         1111
#         1111
# 222233334444
# 222233334444
# 222233334444
# 222233334444
#         55556666
#         55556666
#         55556666
#         55556666

    for r in range(cube_size):
        for c in range(cube_size):
            # face 1
            cube_size[(r + 0 * cube_size, c + 2 * cube_size)] = (r + 0 * cube_size, c + 2 * cube_size)
            # face 2
            # face 3
            # face 4
            cube_size[(r + 2 * cube_size, c + 2 * cube_size)] = (r, c)
            # face 5
            # face 6

    print(part_1(input, get_next_pos_part_1))
    print(part_2(input, get_next_pos_part_2))
