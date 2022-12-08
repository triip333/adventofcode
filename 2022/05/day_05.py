from os import sys, path
import time, re
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
'''

stacks = {}

def load_stacks(input):
    global stacks
    stacks = {}
    lines = input.split('\n\n')[0].splitlines()
    for i in range(1, 10):
        stacks[i] = []
    lines.pop()
    while lines:
        line = lines.pop()
        line = [line[i * 4:i * 4 + 4] for i in range(len(line) // 4 + 1)]
        for i, crate in enumerate(line):
            m = re.search('\w', crate)
            if m:
                stacks[i + 1].append(m.group())


def part_1(input):
    for line in input.split('\n\n')[1].splitlines():
        count, _from, _to = re.findall('\d+', line)
        for _ in range(int(count)):
            stacks[int(_to)].append(stacks[int(_from)].pop())
    res = ''
    for stack in stacks.values():
        res += stack[-1]
    return res


def part_2(input):
    for line in input.split('\n\n')[1].splitlines():
        count, _from, _to = re.findall('\d+', line)
        temp = []
        for _ in range(int(count)):
            temp.append(stacks[int(_from)].pop())
        while temp:
            stacks[int(_to)].append(temp.pop())

    res = ''
    for stack in stacks.values():
        res += stack[-1]
    return res

if __name__ == '__main__':
    input = get_input()
    load_stacks(input)
    print(part_1(input))
    load_stacks(input)
    print(part_2(input))      
