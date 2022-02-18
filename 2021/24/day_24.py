from os import sys, path
from time import perf_counter
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
from collections import defaultdict
from datetime import datetime

def set_value(variable, value):
    global w, x, y, z
    if variable == 'w':
        w = value
    elif variable == 'x':
        x = value
    elif variable == 'y':
        y = value
    elif variable == 'z':
        z = value

def get_value(variable):
    global w, x, y, z
    if variable == 'w':
        return w
    elif variable == 'x':
        return x
    elif variable == 'y':
        return y
    elif variable == 'z':
        return z
    else:
        return int(variable)

def calc(code, input, _z):
    global w, x, y, z
    w, x, y, z = input, _z % 26, 0, _z

    for p in code:
        l = p.split(' ')
        cmd, a = l[0], l[1]
        if len(l) == 3:
            b = l[2]
        # inp a - Read an input value and write it to variable a.
        if cmd == 'inp':
            set_value(a, input)
        # add a b - Add the value of a to the value of b, then store the result in variable a.
        elif cmd == 'add':
            set_value(a, get_value(a) + get_value(b))
        # mul a b - Multiply the value of a by the value of b, then store the result in variable a.
        elif cmd == 'mul':
            set_value(a, get_value(a) * get_value(b))
        # div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
        elif cmd == 'div':
            set_value(a, get_value(a) // get_value(b))
        # mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
        elif cmd == 'mod':
            set_value(a, get_value(a) % get_value(b))
        # eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
        elif cmd == 'eql':
            set_value(a, 1 if get_value(a) == get_value(b) else 0)
    return z

def get_prog(input):
    input = input.splitlines()
    for _ in range(14):
        lines = []
        for _ in range(18):
            lines.append(input.pop(0))
        lines = lines[4:]
        if lines[0] == 'div z 1':
            lines.pop(0)
        yield lines

def check_input(input):
    input = input.splitlines()
    begin = input[:4]
    for _ in range(14):
        l = []
        for i in range(18):
            line = input.pop(0)
            if i < 4:
                assert line == begin[i], f'{line} {begin[i]}'
            l.append(line)
        for line in l:
            if 'y' in line:
                assert line == 'mul y 0'
                break

def part_1(input):
    res = []
    check_input(input)
    D = {}
    D[0] = 0

    for step, prog in enumerate(get_prog(input)):
        starttime = perf_counter()
        N = defaultdict(list)
        for _z, v in D.items():
            for i in range(1, 10):
                z = calc(prog, i, _z)
                if step == 13 and z == 0:
                    res.append(10 * v + i)
                    print(10 * v + i)
                N[z].append(10 * v + i)
        D.clear()
        for k, v in N.items():
            D[k] = min(v)
        print(len(str(D[z])), len(D))
        print(f'time elapsed {((perf_counter() - starttime)):.3f} s\n')
        print(datetime.now())
    return min(res)

def part_2(input):
    return None

if __name__ == '__main__':
    input = get_input()
    print(part_1(input))
