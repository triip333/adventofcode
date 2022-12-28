from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_s
from collections import deque, defaultdict
from functools import cache
sample = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

class Rock():
    def __init__(self, area, height, width):
        self.area = area
        self.height = height
        self.width = width

rocks = []
rocks.append(Rock([(0, 0), (0, 1), (0, 2), (0, 3)], 1, 4))
rocks.append(Rock([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)], 3, 3))
rocks.append(Rock([(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)], 3, 3))
rocks.append(Rock([(0, 0), (1, 0), (2, 0), (3, 0)], 4, 1))
rocks.append(Rock([(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2))

tower_height = 0
calc_count = 0
t = time.perf_counter()

tower = {}
def draw(stopped_rocks, delta_r):
    tower_height
    for r in range(min(p[0] for p in stopped_rocks), max(p[0] for p in stopped_rocks) + 1):
        line = ''
        for c in range(0, 7):
            if (r, c) in stopped_rocks:
                line += '#'
            else:
                line += '.'
        # if (r + tower_height) in tower:
        #     assert tower[r + tower_height] == line, f'{r + tower_height} {line}'
        # else:
        if r < min(p[0] for p in stopped_rocks) + 10:
            tower[r + tower_height] = line
    #     print(f'{(r + tower_height):6d} |{line}|')
    # print()

def draw_rock(rock):
    for r in range(rock.height):
        line = ''
        for c in range(rock.width):
            line += '@' if (r, c) in rock.area else ' '
        #     print(line)
        # print()

@cache
def get_state(gas_position, rock_no, prev_state):
    # def get_pattern(pos, length):
    #     pos = pos % ln
    #     res = input[pos: pos + length]
    #     if len(res) < length:
    #         res += input[0:length - ln]
    #     return res
    #     get_pattern(gas_position, 100)

    global calc_count
    calc_count += 1
    delta_gas = 0

    stopped_rocks = deque(prev_state, 105)
    min_rock_r = min(p[0] for p in stopped_rocks)

    def add_rock(r, c, rock):
        for dr, dc in rock.area:
            stopped_rocks.append((r + dr, c + dc))

    def is_touching(r, c, rock):
        for dr, dc in rock.area:
            if (r + dr, c + dc) in stopped_rocks:
                return True
        return False

    rock = rocks[rock_no]
    # draw_rock(rock)
    rock_r = min_rock_r - rock.height - 3
    rock_c = 2
    while True:
        gas = 1 if input[(gas_position + delta_gas) % len(input)] == '>' else -1
        # print(jet_pattern[delta_gas], end=' ')
        delta_gas += 1

        if 0 <= rock_c + gas and rock_c + rock.width + gas <= 7:
            if not is_touching(rock_r, rock_c + gas, rock):
                rock_c += gas
        if is_touching(rock_r + 1, rock_c, rock):
            add_rock(rock_r, rock_c, rock)

            delta_r = min(sr[0] for sr in stopped_rocks) - min_rock_r

            l = []
            for sr in stopped_rocks:
                l.append((sr[0] - delta_r, sr[1]))

            # print()
            # draw(l, delta_r)
            return delta_r, delta_gas, tuple(l)
        else:
            rock_r += 1
    
h_dict = defaultdict(list)
@measure_s
def solve(input, num):
    global tower_height
    stopped_rocks = tuple([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
    ln = len(input)

    tower_height = 0
    gas_position = 0

    deltas = []

    d = defaultdict(int)
    t = time.perf_counter()
    tick = 0
    prev_value = tower_height
    i = 0
    n = (num - 470) // 1735
    n2 = num - n * 1735
    while i < num:
    # for i in range(num):

        # if True:
        for _ in range(n2):
            old_stopped_rocks = stopped_rocks
            delta_r, delta_gas, stopped_rocks = get_state(gas_position, i % 5, stopped_rocks)
            h = hash((old_stopped_rocks, i % 5, stopped_rocks))
            h_dict[h].append((i, abs(tower_height)))
            tower_height += delta_r

            deltas.append(abs(delta_r))

            # draw_rock(rocks[i % 5])
            # print(f'{i:5d} {delta_r=}')
            # draw(stopped_rocks, delta_r)
            gas_position += delta_gas % ln
            # i += 1
            # print(i, abs(tower_height), end='\t')
        
        return n * 2781 + abs(tower_height)

    #     # n = (num - 10000) // 2205
    #     # if i == num - 2205 * n:
    #     #     print(f'{(num - 5000) // 2205=}')
    #     #     print(f'{i=}')
    #     #     print(f'{num - 2205 * n=}')
    #     #     return abs(tower_height) + n * 2781
        

    #     # if i % 2205 == 775:
    #     #     print(i, abs(tower_height), abs(tower_height) - prev_value)
    #     #     prev_value = abs(tower_height)

    #     # if i == 1102 + 1 * 2205:
    #     # # if abs(tower_height) == 1745:
    #     #     print(i)
    #     #     return abs(tower_height)


    #     # print(f'{i:5d} {(abs(tower_height) / (i + 1)):.6f}')
    # # print(deltas)
    # c = 0
    # for k in sorted(h_dict, key=lambda x: len(h_dict[x]), reverse=True):
    #     print(k, h_dict[k])
    #     # if h_dict[k] > 1:
    #     #     c += 1
    #     for a, b in zip(h_dict[k][:-1], h_dict[k][1:]):
    #         print(b[1] - a[1], end=' ')
    #     print()
    #     if len(h_dict[k]) == 1:
    #         c += 1
    # print(num, c)

    # for c in range(5):
    #     for k in sorted(d, key=lambda x: d[x], reverse=True):
    #         if k[0] == c:
    #             print(k, d[k], '\t', len(k[1]))
    # print(len(d))
    return abs(tower_height)

if __name__ == '__main__':
    input = get_input()
    # input = sample
    # print(solve(input, 10000))
    print(solve(input, 2022))
    # for i in range(10, 200):
    #     print(solve(input, i * 1000))

    # for k in sorted(tower.keys()):
    #     print(f'{(k):6d} |{tower[k]}|')

    # d = defaultdict(int)
    # for k, v in tower.items():
    #     d[v] += 1
    # for k, v in d.items():
    #     print(k, v)

    # print(solve(input, 100000))
    print(solve(input, 1000000000000))
