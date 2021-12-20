from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i\
'''

def solve(input):
    D = {}
    l = []
    for line in input.split('\n'):
        op, w = line.split(' -> ')
        if op.isnumeric():
            D[w] = int(op)
        else:
            l.append((op, w))
    while len(l) > 0:
        for i, j in enumerate(l):
            op = j[0]
            w = j[1]
            if 'AND' in op:
                x, _, y = op.split()
                if x.isnumeric():
                    x = int(x)
                elif x in D:
                    x = D[x]
                else:
                    continue
                if y in D:
                    D[w] = x & D[y]
                    l.pop(i)
            elif 'OR' in op:
                x, _, y = op.split()
                if x in D and y in D:
                    D[w] = D[x] | D[y]
                    l.pop(i)
            elif 'NOT' in op:
                _, y = op.split()
                if y in D:
                    D[w] = ~ D[y]
                    l.pop(i)
            elif 'LSHIFT' in op:
                x, _, y = op.split()
                assert y.isnumeric()
                if x in D:
                    D[w] = D[x] << int(y)
                    l.pop(i)
            elif 'RSHIFT' in op:
                x, _, y = op.split()
                assert y.isnumeric()
                if x in D:
                    D[w] = D[x] >> int(y)
                    l.pop(i)
            elif len(op.split()) == 1 and op in D:
                D[w] = D[op]
        if 'a' in D:
            return D['a']

if __name__ == '__main__':
    input = get_input()
    # input = sample
    a = solve(input)
    print(a)
    print(solve(input.replace('44430 -> b', f'{a} -> b')))      
