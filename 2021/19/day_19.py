from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
from itertools import permutations
from collections import defaultdict
from functools import cache
from common import measure_s

with open('sample') as f:
    sample = f.read()

class Configuration():
    def __init__(self, i, j, k, x, y, z):
        self.i = i
        self.j = j
        self.k = k
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        ch = 'xyz'
        return f'{self.i}, {self.j}, {self.k} [{ch[self.x]} {ch[self.y]} {ch[self.z]}]'

    def conv_beacon(self, b):
        assert len(b) == 3
        return [self.i * b[self.x], self.j * b[self.y], self.k * b[self.z]]

class Scanner():
    def __init__(self, line):
        line = line.splitlines()
        self.desc = line.pop(0)
        self.beacons = []
        for l in line:
            self.beacons.append([int(i) for i in l.split(',')])
        self.conf = None
        self.__absolute_coords = None
        self.x_offset = 0
        self.y_offset = 0
        self.z_offset = 0
    
    def __str__(self):
        res = self.desc + '\n'
        res += f'conf: {str(self.conf)}\n'
        res += f'offset: {self.x_offset} {self.y_offset} {self.z_offset}\n'
        if self.absolute_coords():
            res += f'beacons: {str(sorted(self.absolute_coords()))}\n'
        return res

    def absolute_coords(self):
        if not self.__absolute_coords:
            self.__absolute_coords = []
            for b in self.beacons:
                x, y, z = self.conf.conv_beacon(b)
                self.__absolute_coords.append([x + self.x_offset, y + self.y_offset, z + self.z_offset])
        return self.__absolute_coords
    
    def configurations(self):
        for i in [-1, 1]:
            for j in [-1, 1]:
                for k in [-1, 1]:
                    for x, y, z in permutations(range(3)):
                        yield Configuration(i, j, k, x, y, z)

    @cache
    # @measure_ms
    def find_conf(self, zero):
        print(f'  find {self.desc}')
        for z_x, z_y, z_z in zero.absolute_coords():
            for conf in self.configurations():
                for i in range(len(self.beacons)):
                    b_x, b_y, b_z = conf.conv_beacon(self.beacons[i])
                    x_offset, y_offset, z_offset = z_x - b_x, z_y - b_y, z_z - b_z
                    same_count = 0
                    for b in self.beacons:
                        t_x, t_y, t_z = conf.conv_beacon(b)
                        if [t_x + x_offset, t_y + y_offset, t_z + z_offset] in zero.absolute_coords():
                            same_count += 1
                    if same_count >= 12:
                        self.conf = conf
                        self.x_offset, self.y_offset, self.z_offset = x_offset, y_offset, z_offset
                        return True

@measure_s
def solution():
    input = get_input()
    # input = sample
    lst = input.split('\n\n')
    scanners = []
    for l in lst:
        scanners.append(Scanner(l))

    scanners[0].conf = Configuration(1, 1, 1, 0, 1, 2)
    while not all([s.conf for s in scanners]):
        for zero in [s for s in scanners if s.conf]:
            print(f'zero {zero.desc}')
            for s in [s for s in scanners if not s.conf]:
                if s.find_conf(zero):
                    print(str(s))
                    # pass

    MAP = defaultdict(int)
    for s in scanners:
        for a in s.absolute_coords():
            MAP[tuple(a)] += 1
    print(len(MAP))

    distance = 0
    for s1 in scanners:
        for s2 in scanners:
            if s1 != s2:
                distance = max(distance, abs(s1.x_offset - s2.x_offset) + abs(s1.y_offset - s2.y_offset) + abs(s1.z_offset - s2.z_offset))
    print(distance)

if __name__ == '__main__':
  solution()