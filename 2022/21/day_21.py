from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
'''

d = {}

def get_value(key):
    res = d[key]
    if res.isnumeric():
        return int(res)
    else:
        a, op, b = res.split()
        if op == '+':
            return get_value( a ) + get_value( b )
        elif op == '-':
            return get_value( a ) - get_value( b )
        elif op == '*':
            return get_value( a ) * get_value( b )
        elif op == '/':
            a = get_value( a )
            b = get_value( b )
            assert a % b == 0
            return a // b
        

def has_humn(key):
    if key == 'humn':
        return True
    res = d[key]
    if res.isnumeric():
        return False
    else:
        a, _, b = res.split()
        return has_humn(a) or has_humn(b)


def set_humn_value(key, val):
    if key == 'humn':
        d['humn'] = val
    else:
        a, op, b = d[key].split()
        if has_humn(a):
            if op == '+':
                set_humn_value(a, val - get_value(b))
            elif op == '-':
                set_humn_value(a, val + get_value(b))
            elif op == '*':
                assert val % abs(get_value(b)) == 0
                set_humn_value(a, val // get_value(b))
            elif op == '/':
                set_humn_value(a, val * get_value(b))
        if has_humn(b):
            if op == '+':
                set_humn_value(b, val - get_value(a))
            elif op == '-':
                set_humn_value(b, get_value(a) - val)
            elif op == '*':
                assert val % get_value(a) == 0
                set_humn_value(b, val // get_value(a))
            elif op == '/':
                assert val % get_value(a) == 0
                set_humn_value(b, val // get_value(a))


def part_1(input):
    return get_value('root')


def part_2(input):
    a, _, b = d['root'].split()
    if has_humn(a):
        set_humn_value(a, get_value(b))
    if has_humn(b):
        set_humn_value(b, get_value(a))
    return d['humn']


if __name__ == '__main__':
    input = get_input()
    # input = sample
    for line in input.splitlines():
        line = line.strip().split(': ')
        d[line[0]] = line[1]
    print(part_1(input))
    print(part_2(input))
