from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms, measure_s
from functools import reduce
import re
from itertools import permutations

sample = '''\
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]\
'''

def explode(num):
    nest_level = 0
    pos_start, pos_end = 0, len(num)
    for i, ch in enumerate(num):
        if ch == '[':
            nest_level += 1
            pos_start = i
        elif ch == ']':
            if nest_level > 4:
                pos_end = i + 1
                i, j = [int(s) for s in num[pos_start + 1:pos_end - 1].split(',')]
                res_str_a, res_str_b = num[:pos_start], num[pos_end:]
                match = None
                for m in re.finditer('\d+', res_str_a):
                    match = m.group()
                if match:
                    pos = res_str_a.rfind(match)
                    res_str_a = res_str_a[:pos] + res_str_a[pos:].replace(match, str(int(match) + i), 1)
                m = re.search('\d+', res_str_b)
                if m:
                    res_str_b = res_str_b.replace(m.group(), str(int(m.group()) + j), 1)
                return res_str_a + '0' + res_str_b
            nest_level -= 1
    return num
            
def split(num):
    m = re.search('\d\d+', num)
    if m:
        match = m.group()
        val = int(match)
        return num.replace(match, f'[{val // 2},{(val + 1) // 2}]', 1)
    return num

def add(a, b):
    prev, num = '', f'[{a},{b}]'
    while prev != num:
        while prev != num:
            prev = num
            num = explode(num)
        num = split(num)
    return num

def magnitude(num):
    while True:
        m = re.search('\[\d+,\d+\]', num)
        if not m:
            break
        match = m.group()
        a, b = [int(i) for i in match[1:-1].split(',')]
        num = num.replace(match, str(3 * a + 2 * b), 1)
    return int(num)

@measure_s
def part_1(input):
    l = reduce(lambda a, b: add(a, b), [line for line in input.splitlines()])
    return magnitude(l)

@measure_s
def part_2(input):
    res = []
    for a, b in permutations([line for line in input.splitlines()], 2):
        res.append(magnitude(add(a, b)))
    return max(res)

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))
