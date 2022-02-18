from os import sys, path
from time import perf_counter
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
from collections import defaultdict
from datetime import datetime

def get_prog(input):
    input = input.splitlines()
    for i in range(14):
        lines = []
        for _ in range(18):
            lines.append(input.pop(0))
        lines = lines[4:]
        if lines[0] == 'div z 1':
            lines.pop(0)
        res = []
        for line in lines:
            cmd, a, b = line.split()
            # add a b - Add the value of a to the value of b, then store the result in variable a.
            if cmd == 'add':
                res.append(f'{a} += {b}')
            # mul a b - Multiply the value of a by the value of b, then store the result in variable a.
            elif cmd == 'mul':
                res.append(f'{a} *= {b}')
            # div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
            elif cmd == 'div':
                res.append(f'{a} //= {b}')
            # mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
            elif cmd == 'mod':
                res.append(f'{a} %= {b}')
            # eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
            elif cmd == 'eql':
                res.append(f'{a} = 1 if {a} == {b} else 0')
        yield compile('\n'.join(res), f'temp_{i}', 'exec')

def check_input(input):
    input = input.splitlines()
    begin = input[:4]
    for _ in range(14):
        lines = []
        for i in range(18):
            line = input.pop(0)
            if i < 4:
                assert line == begin[i], f'{line} {begin[i]}'
            lines.append(line)
        for line in lines:
            if 'y' in line:
                assert line == 'mul y 0'
                break

def solve(input, fn):
    res = []
    check_input(input)
    D = {}
    D[0] = 0

    for step, prog in enumerate(get_prog(input)):
        starttime = perf_counter()
        N = defaultdict(list)
        for _z, v in D.items():
            for i in range(1, 10):
                locals = {'w': i, 'x': _z % 26, 'y': 0, 'z': _z}
                exec(prog, globals(), locals)
                N[locals['z']].append(10 * v + i)
                if step == 13 and locals['z'] == 0:
                    res.append(10 * v + i)
        D.clear()
        for k, v in N.items():
            D[k] = fn(v)
        print('start', len(str(D[k] + 1)), datetime.now())
        print(f'time elapsed {((perf_counter() - starttime)):.3f} s\n')
    return(fn(res))

if __name__ == '__main__':
    input = get_input()
    print('result', solve(input, max))
    print('result', solve(input, min))    