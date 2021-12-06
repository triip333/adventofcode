from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
from collections import defaultdict

sample = '''\
3,4,3,1,2\
'''

def part_1(input):
    lst = [int(i) for i in input.split(',')]
    for day in range(80):
        starttime = time.perf_counter()
        cnt = 0
        for i, j in enumerate(lst):
            if j == 0:
                lst[i] = 6
                cnt += 1
            else:
                lst[i] = j - 1
        lst += cnt * [8] 
        # print(f'day {day + 1} {len(lst)} {((time.perf_counter() - starttime)):.3f} s')
    return len(lst)
 
def part_2(input):
    D = defaultdict(int)
    lst = [int(i) for i in input.split(',')]
    for i in input.split(','):
        D[int(i)] += 1

    for day in range(256):
        C = defaultdict(int)
        for i in range(9):
            if i == 0:
                C[6] += D[0]
                C[8] += D[0]
            else:
                C[i - 1] += D[i]
        D = C
        # print(f'day {day + 1} {D.values()}')
    return sum(D.values())

if __name__ == '__main__':
    input  = get_input()
    # print(part_1(sample))
    print(part_1(input))
    # print(part_2(sample))
    print(part_2(input))      
