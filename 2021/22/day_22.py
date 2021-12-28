from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms
from collections import defaultdict

sample = '''\
on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10\
'''

def parse(line):
    state = line.startswith('on')
    x, y, z = [s[2:] for s in line.split()[1].split(',')]
    x1, x2 = int(x.split('..')[0]), int(x.split('..')[1])
    y1, y2 = int(y.split('..')[0]), int(y.split('..')[1])
    z1, z2 = int(z.split('..')[0]), int(z.split('..')[1])
    assert x1 <= x2
    assert y1 <= y2
    assert z1 <= z2
    return state, x1, x2, y1, y2, z1, z2

class Cube():
    def __init__(self, state, x1, x2, y1, y2, z1, z2):
        self.state = state
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2

    def __str__(self):
        return f'x={self.x1}..{self.x2} y={self.y1}..{self.y2} y={self.z1}..{self.z2}'

    def overlaps_with(self, c):
        x = self.x1 <= c.x2 and c.x1 <= self.x2
        y = self.y1 <= c.y2 and c.y1 <= self.y2
        z = self.z1 <= c.z2 and c.z1 <= self.z2
        return x and y and z

    def contains_within(self, c):
        x = c.x1 <= self.x1 <= self.x2 <= c.x2
        y = c.y1 <= self.y1 <= self.y2 <= c.y2
        z = c.z1 <= self.z1 <= self.z2 <= c.z2
        return x and y and z

    def split_cube(self, c):
        res = []
        t = Cube(self.state, self.x1, self.x2, self.y1, self.y2, self.z1, self.z2)
        if t.x1 < c.x1 <= t.x2:
            res.append(Cube(t.state, t.x1, c.x1 - 1, t.y1, t.y2, t.z1, t.z2))
            t = Cube(t.state, c.x1, t.x2, t.y1, t.y2, t.z1, t.z2)
        if t.x1 <= c.x2 < t.x2:
            res.append(Cube(self.state, c.x2 + 1, t.x2, t.y1, t.y2, t.z1, t.z2))
            t = Cube(t.state, t.x1, c.x2, t.y1, t.y2, t.z1, t.z2)
        if t.y1 < c.y1 <= t.y2:
            res.append(Cube(t.state, t.x1, t.x2, t.y1, c.y1 - 1, t.z1, t.z2))
            t = Cube(t.state, t.x1, t.x2, c.y1, t.y2, t.z1, t.z2)
        if t.y1 <= c.y2 < t.y2:
            res.append(Cube(self.state, t.x1, t.x2, c.y2 + 1, t.y2, t.z1, t.z2))
            t = Cube(t.state, t.x1, t.x2, t.y1, c.y2, t.z1, t.z2)
        if t.z1 < c.z1 <= t.z2:
            res.append(Cube(t.state, t.x1, t.x2, t.y1, t.y2, t.z1, c.z1 - 1))
            t = Cube(t.state, t.x1, t.x2, t.y1, t.y2, c.z1, t.z2)
        if t.z1 <= c.z2 < t.z2:
            res.append(Cube(self.state, t.x1, t.x2, t.y1, t.y2, c.z2 + 1, t.z2))
            t = Cube(t.state, t.x1, t.x2, t.y1, t.y2, t.z1, c.z2)
        res.append(t)
        return res
    
    def size(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)

@measure_ms
def part_1(input):
    S = set()
    for line in input.splitlines():
        c = Cube(*parse(line))
        if -50 < c.x2 and c.x1 < 50 and -50 < c.y2 and c.y1 < 50 and -50 < c.z2 and c.z1 < 50:
            for x in range(c.x1, c.x2 + 1):
                for y in range(c.y1, c.y2 + 1):
                    for z in range(c.z1, c.z2 + 1):
                        if -50 <= c.x1 <= 50 and -50 <= c.x2 <= 50 and -50 <= c.y1 <= 50 and -50 <= c.y2 <= 50 and -50 <= c.z1 <= 50 and -50 <= c.z2 <= 50:
                            if c.state:
                                S.add((x, y, z))
                            elif (x, y, z) in S:
                                S.remove((x, y, z))
    return len(S)

@measure_ms
def part_2(input):
    cubes = []
    for line in input.splitlines():
        cube = Cube(*parse(line))
        new_cubes = []
        while len(cubes) > 0:
            c = cubes.pop(0)
            if c.contains_within(cube):
                pass
            elif c.overlaps_with(cube):
                # assert c.size() == sum([temp.size() for temp in c.split_cube(cube)])
                cubes += c.split_cube(cube)
            else:
                new_cubes.append(c)
        if cube.state:
            new_cubes.append(cube)
        cubes = new_cubes
    return sum([c.size() for c in cubes])

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))      
