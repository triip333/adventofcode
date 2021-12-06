from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
3,4,3,1,2\
'''

def part_1(input):
    lst = [int(i) for i in input.split(',')]
    print(lst)
    for day in range(2560):
        starttime = time.perf_counter()
        cnt = 0
        for i, j in enumerate(lst):
            if j == 0:
                lst[i] = 6
                cnt += 1
            else:
                lst[i] = j - 1
        lst += cnt * [8] 
        print(f'day {day + 1} {len(lst)} {((time.perf_counter() - starttime)):.3f} s')
    return len(lst)
 
def part_2(input):
    lst = [int(i) for i in input.split(',')]
    c0 = lst.count(0)
    c1 = lst.count(1)
    c2 = lst.count(2)
    c3 = lst.count(3)
    c4 = lst.count(4)
    c5 = lst.count(5)
    c6 = lst.count(6)
    c7 = lst.count(7)
    c8 = lst.count(8)

    print(lst)
    for day in range(256):
        l = [c0, c1, c2, c3, c4, c5, c6, c7, c8]
        c0 = l[1]
        c1 = l[2]
        c2 = l[3]
        c3 = l[4]
        c4 = l[5]
        c5 = l[6]
        c6 = l[7] + l[0]
        c7 = l[8]
        c8 = l[0]
        # print(f'day {day + 1} {sum([c0, c1, c2, c3, c4, c5, c6, c7, c8])}')
    return sum([c0, c1, c2, c3, c4, c5, c6, c7, c8])

if __name__ == '__main__':
    input  = get_input()
    print(part_1(sample))
    # print(part_1(input))
    print(part_2(sample))
    # print(part_2(input))      
