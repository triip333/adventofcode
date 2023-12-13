from os import sys, path
import re
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''

def part_1(input):
    res = 0
    for line in input.splitlines():
        numbers = [int(i) for i in re.findall('-?\d+', line)]
        next_values = []
        while any(numbers):
            cur = []
            next_values.append(numbers[-1])
            for i in range(1, len(numbers)):
                cur.append(numbers[i] - numbers[i - 1])
            numbers = cur
        next_value = 0
        while next_values:
            next_value += next_values.pop()
        res += next_value
    return res

def part_2(input):
    res = 0
    for line in input.splitlines():
        numbers = [int(i) for i in re.findall('-?\d+', line)]
        prev_values = []
        while any(numbers):
            cur = []
            prev_values.append(numbers[0])
            for i in range(1, len(numbers)):
                cur.append(numbers[i] - numbers[i - 1])
            numbers = cur
        prev_value = 0
        while prev_values:
            prev_value = prev_values.pop() - prev_value
        res += prev_value
    return res

if __name__ == '__main__':
    input = get_input()
    # input = sample.rstrip()
    print(part_1(input))
    print(part_2(input))
