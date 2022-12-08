from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

priorities = ['']

def part_1(input):
    res = 0
    for line in input.splitlines():
        a, b = line[:len(line)//2], line[len(line)//2:]
        shared = []
        for ch in a:
            if ch in b:
                shared.append(ch)
        res += priorities.index(shared[0])
    return res

def part_2(input):
    res = 0
    lines = input.splitlines()
    while lines:
        a, b, c = lines.pop(0), lines.pop(0), lines.pop(0)
        for ch in a:
            if ch in b and ch in c:
                res += priorities.index(ch)
                break
    return res

if __name__ == '__main__':
    input = get_input()
    # input = sample
    for i in range(26):
        priorities.append(chr(ord('a') + i))
    for i in range(26):
        priorities.append(chr(ord('A') + i))

    print(part_1(input))
    print(part_2(input))      
