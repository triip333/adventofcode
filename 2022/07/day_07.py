from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
from collections import defaultdict

sample = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''

def solve(input):
    lines = input.splitlines()
    lines.pop(0)
    file_system = defaultdict(int)
    cur_dir = ''
    while lines:
        line = lines.pop(0)
        if line.startswith('$ cd '):
            dir_to = line.split()[2]
            if dir_to == '..':
                cur_dir = '/'.join(cur_dir.split('/')[:-1])
            else:
                cur_dir = f'{cur_dir}/{dir_to}'
        elif line.startswith('$ ls'):
            while lines and not lines[0].startswith('$'):
                line = lines.pop(0)
                if line.startswith('dir'):
                    file_system[f"{cur_dir}/{line.split()[1]}"] += 0
                else:
                    file_system[f"{cur_dir if cur_dir else '/'}"] += int(line.split()[0])

    res = defaultdict(int)
    for k, v in sorted(file_system.items()):
        if k != '/':
            res['/'] += v
        k = k[1:]
        dir = k.split('/')
        while dir:
            res['/' + '/'.join(dir)] += v
            dir = dir[:-1]

    space_needed = abs(70000000 - 30000000 - res['/'])

    return sum([size for size in res.values() if size <= 100000]), min([size for size in res.values() if size >= space_needed])

def part_2(input):
    return None

if __name__ == '__main__':
    input = get_input()
    # input = sample
    for res in solve(input):
        print(res)