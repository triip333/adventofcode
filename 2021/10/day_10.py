from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms
from collections import defaultdict

sample = '''\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]\
'''

incomplete_list = []

@measure_ms
def part_1(input):
    res = 0
    D = defaultdict(int)
    for line in input.split():
        ln = 0
        while ln != len(line):
            ln = len(line)
            line = line.replace('()', '')
            line = line.replace('[]', '')
            line = line.replace('{}', '')
            line = line.replace('<>', '')
        corrupted = False
        for ch in line:
            if ch in ')]}>':
                res += {')': 3, ']': 57, '}': 1197, '>': 25137}[ch]
                corrupted = True
                break
        if not corrupted:
            incomplete_list.append(line)
    return res

@measure_ms
def part_2(input):
    score = []
    for line in incomplete_list:
        res = 0
        l = [ch for ch in line]
        while len(l) > 0:
            ch = l.pop()
            res = res * 5 + {'(': 1, '[': 2, '{': 3, '<': 4}[ch]
        score.append(res)
    return sorted(score)[int(len(score) / 2)]

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))      
