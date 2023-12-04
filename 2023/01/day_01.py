from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''

sample = '''\
ztgszqjjsrtmgqx6572
'''

D = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def part_1(input):
    res = 0
    for line in input.splitlines():
        l = [ch for ch in line if ch.isdigit()]
        res += int(l[0] + l[-1])
    return res

def part_2(input):
    def isdigit(word):
        pass

    res = 0
    for line in input.splitlines():
        a, b = None, None

        for i in range(len(line)):
            if line[i].isdigit():
                a = line[i]
            else:
                for d in D.keys():
                    if d in line[:i + 1]:
                        a = D[d]
            if a:
                break

        for i in range(-1, -(len(line) + 1), -1):
            if line[i].isdigit():
                b = line[i]
            else:
                for d in D.keys():
                    if d in line[i:]:
                        b = D[d]
            if b:
                break

        res += int(a + b)
    return res

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))