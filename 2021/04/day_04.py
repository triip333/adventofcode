from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms

sample = '''\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''

class Bingo():
    def __init__(self, line):
        self.arr = [[[int(i), False] for i in l.split()] for l in line.split('\n')]
        self.last_num = 0
    
    def __str__(self):
        res = ''
        for i in range(5):
            for j in range(5):
                a = self.arr[i][j]
                res += f'({str(self.arr[i][j][0]).rjust(2)} {str(self.arr[i][j][1]).ljust(5)}) '
            res += '\n'
        return res
    
    def add_number(self, num):
        self.last_num = num
        for i in range(5):
            for j in range(5):
                if self.arr[i][j][0] == num:
                    self.arr[i][j][1] = True
                    return

    def is_complete(self):
        for i in range(5):
            if all([self.arr[i][j][1] for j in range(5)]):
                return True
        for j in range(5):
            if all([self.arr[i][j][1] for i in range(5)]):
                return True

    def value(self):
        res = 0
        for i in range(5):
            for j in range(5):
                if not self.arr[i][j][1]:
                    res += self.arr[i][j][0]
        return f'{res} * {self.last_num} = {res * self.last_num}'

@measure_ms
def part_1(input):
    lst = input.split('\n\n')
    numbers = lst.pop(0).split(',')
    boards = []
    for l in lst:
        boards.append(Bingo(l))

    for num in [int(i) for i in numbers]:
        for b in boards:
            b.add_number(num)
            if b.is_complete():
                return b.value()

@measure_ms
def part_2(input):
    lst = input.split('\n\n')
    numbers = lst.pop(0).split(',')
    boards = []
    for l in lst:
        boards.append(Bingo(l))

    for num in [int(i) for i in numbers]:
        for b in boards:
            b.add_number(num)
        
        if len(boards) > 1:
            br = []
            for b in boards:
                if not b.is_complete():
                    br.append(b)
                else:
                    pass
            boards = br

        if len(boards) == 1 and boards[0].is_complete():
            return boards[0].value()

if __name__ == '__main__':
    input = get_input()
    # input sample
    print(part_1(input))
    print(part_2(input))      
