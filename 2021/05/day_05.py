from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2\
'''

class Data():
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    step_x = 0
    step_y = 0

    def __init__(self, line):
        first, second = line.split(' -> ')
        self.x1, self.y1 = [int(i) for i in first.split(',')]
        self.x2, self.y2 = [int(i) for i in second.split(',')]
        self.step_x = 1 if self.x1 <= self.x2 else -1
        self.step_y = 1 if self.y1 <= self.y2 else -1
    
    def __str__(self):
        return f'{self.x1},{self.y1} -> {self.x2},{self.y2}'
    
    def get_point(self):
        x = self.x1
        y = self.y1
        while not ((x == self.x2) and (y == self.y2)):
            yield x, y
            if self.x1 != self.x2:
                x += self.step_x
            if self.y1 != self.y2:
                y += self.step_y
        yield x, y

def parse(input):
    global D
    D = []
    for line in input.split('\n'):
        D.append(Data(line))

    max_x, max_y = 0, 0
    for d in D:
        if d.x1 > max_x:
            max_x = d.x1
        if d.y1 > max_y:
            max_y = d.y1    
        if d.x2 > max_x:
            max_x = d.x2
        if d.y2 > max_y:
            max_y = d.y2

    global arr
    arr = [[0 for j in range(max_x + 1)] for i in range(max_y + 1)]

def part_1(input):
    parse(input)
    for d in D:
        if (d.x1 == d.x2) or (d.y1 == d.y2):
            for i, j in d.get_point():
                arr[j][i] += 1

    return sum([1 if i > 1 else 0 for a in arr for i in a])

def part_2(input):
    parse(input)
    for d in D:
        for i, j in d.get_point():
            arr[j][i] += 1
    return sum([1 if i > 1 else 0 for a in arr for i in a])

if __name__ == '__main__':
    input  = get_input()
    print(part_1(sample))
    print(part_2(sample))      
    # print(part_1(input))
    # print(part_2(input))      
