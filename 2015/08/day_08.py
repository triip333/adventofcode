from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
""
"abc"
"aaa\\"aaa"
"\\x27"\
'''

def get_chars(line):
    assert line[0] == '"'
    assert line[-1] == '"'
    line = line[1:-1]
    while line:
        if line[0] == '\\':
            if line[1] == 'x':
                line = line[4:]
                yield 1
            else:
                line = line[2:]
                yield 1
        else:
            line = line[1:]
            yield 1

def part_1(input):
    res = 0
    for line in input.strip().splitlines():
        res += len(line) - sum([x for x in get_chars(line)])
    return res

def escape_str(line):
    res = ''
    for ch in line:
        if ch == '"':
            res += '\\"'
        elif ch == '\\':
            res += '\\\\'
        else:
            res += ch
    return f'"{res}"'

def part_2(input):
    res = 0
    for line in input.strip().splitlines():
        res += len(escape_str(line)) - len(line)
    return res

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))