from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms

sample = '''\
start-A
start-b
A-c
A-b
b-d
A-end
b-end\
'''

def get_neighbors(current_cave):
    for c in caves:
        if c[0] == current_cave and c[1] != 'start':
            yield c[1]
        elif c[1] == current_cave and c[0] != 'start':
            yield c[0]

def is_valid_1(next_cave, current_path):
    return not (next_cave.islower() and next_cave in current_path)

def is_valid_2(next_cave, current_path):
    if not next_cave.islower():
        return True
    doubles = 0
    new_path = current_path + [next_cave]
    for p in set(new_path):
        if p.islower():
            if new_path.count(p) > 2:
                return False
            if new_path.count(p) == 2:
                doubles += 1
    return doubles <= 1

@measure_ms
def solve(is_valid_func):
    path = [['start']]
    while True:
        new_path = []
        for p in path:
            if p[-1] == 'end':
                new_path.append(p)
            else:
                for n in get_neighbors(p[-1]):
                    if is_valid_func(n, p):
                        new_path.append(p + [n])
        if len(path) == len(new_path):
            break
        else:
            path = new_path
    return len(path)

if __name__ == '__main__':
    input = get_input()
    # input = sample
    caves = []
    for line in input.split():
        caves.append(tuple(line.split('-')))

    print(solve(is_valid_1))
    print(solve(is_valid_2))
