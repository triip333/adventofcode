from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
from functools import cmp_to_key

sample = '''\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
'''

def compare(left, right):
    if len(left) == 0 and len(right) > 0:
        return 1
    elif len(left) > 0 and len(right) == 0:
        return -1
    elif len(left) == 0 and len(right) == 0:
        return 0
    else:
        while left and right:
            a = left.pop(0)
            b = right.pop(0)
            res = 0
            if isinstance(a, int) and isinstance(b, list):
                a = [a]
            elif isinstance(a, list) and isinstance(b, int):
                b = [b]
            if isinstance(a, list) and isinstance(b, list):
                res = compare(a, b)
                if res == 0:
                    return compare(left, right)
                else:
                    return res
            elif isinstance(a, int) and isinstance(b, int):
                if a > b:
                    return -1
                elif a < b:
                    return 1
                else:
                    res = compare(left, right)
                    if res != 0:
                        return res
        return 0


def part_1(input):
    res = 0
    for i,pair in enumerate(input.split('\n\n')):
        c = compare(eval(pair.splitlines()[0].strip()), eval(pair.splitlines()[1].strip()))
        if c >= 0:
            res += i + 1
    return res


def part_2(input):
    l = ['[[2]]', '[[6]]']
    for line in input.splitlines():
        line = line.strip()
        if line:
            l.append(line)
    l = sorted(l, key=cmp_to_key(lambda a, b: compare(eval(a), eval(b))))[::-1]
    return (l.index('[[2]]') + 1) * (l.index('[[6]]') + 1)


if __name__ == '__main__':
    input = get_input()
    input = sample
    print(part_1(input))
    print(part_2(input))      
