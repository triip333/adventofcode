from os import sys, path
import time, re
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''

def part_1(input):
    res = 0
    for line in input.splitlines():
        line = line.split(': ')[1]
        a = set([int(i) for i in re.findall('\d+', line.split(' | ')[0])])
        b = set([int(i) for i in re.findall('\d+', line.split(' | ')[1])])
        r = a & b
        if r:
            res += 2 ** (len(r) - 1)
    return res

def part_2(input):
    d = {}
    l, c = [], []
    for line in input.splitlines():
        line = line.split(': ')
        d[line[0]] = line[1]
        l.append(line[0])
        c.append(1)
    for i, key in enumerate(l):
        a = set([int(i) for i in re.findall('\d+', d[key].split(' | ')[0])])
        b = set([int(i) for i in re.findall('\d+', d[key].split(' | ')[1])])
        for j in range(len(a & b)):
            c[i + j + 1] += c[i]
    return sum(c)

if __name__ == '__main__':
    input = get_input()
    # input = sample.rstrip()
    print(part_1(input))
    print(part_2(input))