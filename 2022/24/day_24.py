from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms
from functools import cache
from collections import deque

sample = '''\
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
'''

START, END = None, None
up, down, left, right = '^', 'v', '<', '>'

@cache
def get_map(time):
    global START, END
    m = []
    if time == 0:
        l = [line.strip()[1:-1] for line in input.splitlines()]
        l.pop(0)
        l.pop()
        for line in l:
            m.append([[] if ch == '.' else [ch] for ch in line])
        START = (-1, 0)
        END = (len(m), len(m[0]) - 1)
    else:
        prev = get_map(time - 1)
        m = [[[] for c in range(len(prev[0]))] for r in range(len(prev))]
        for r in range(len(m)):
            for c in range(len(m[r])):
                while prev[r][c]:
                    ch = prev[r][c].pop()
                    if ch == up:
                        m[(r - 1) % len(prev)][c].append(ch)
                    elif ch == down:
                        m[(r + 1) % len(prev)][c].append(ch)
                    elif ch == left:
                        m[r][(c - 1) % len(prev[r])].append(ch)
                    elif ch == right:
                        m[r][(c + 1) % len(prev[r])].append(ch)
    return m

def get_neighbors(time, pos):
    m = get_map(time + 1)
    for dr, dc in [(1, 0), (0, 1), (0, 0), (-1, 0), (0, -1)]:
        r, c = pos[0] + dr, pos[1] + dc
        if (r, c) in [START, END]:
                yield (r, c)
        elif 0 <= r < len(m) and 0 <= c < len(m[dr]):
            if len(m[r][c]) == 0:
                yield (r, c)

def draw_map(time, m):
    print(f'Minute {time}')
    for r in range(len(m)):
        line = ''
        for c in range(len(m[r])):
            if len(m[r][c]) == 0:
                line += '.'
            elif len(m[r][c]) == 1:
                line += m[r][c][0]
            else:
                line += str(len(m[r][c]))
        print(line)
    print()

@measure_ms
def solve():
    time = 0
    get_map(0)
    for start, end in [(START, END), (END, START), (START, END)]:
        queue = deque([(time, start)])
        visited = set((time, start))
        while queue:
            time, pos = queue.popleft()
            for new_pos in get_neighbors(time, pos):
                if new_pos == end:
                    if new_pos == END:
                        print(time + 1)
                    time = time + 1
                    queue = None
                    break
                elif not (time + 1, new_pos) in visited:
                    visited.add((time + 1, new_pos))
                    queue.append((time + 1, new_pos))
    return time 

if __name__ == '__main__':
    input = get_input()
    # input = sample
    solve()