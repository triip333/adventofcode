from os import sys, path
import re
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_s

sample = '''\
Time:      7  15   30
Distance:  9  40  200
'''

@measure_s
def solve(input):
    res = 1
    input = input.splitlines()
    times = [int(i) for i in re.findall('\d+', input.pop(0))]
    distances = [int(i) for i in re.findall('\d+', input.pop(0))]
    while times and distances:
        time = times.pop(0)
        distance = distances.pop(0)
        wins = 0
        for i in range(1, time):
            if i * (time - i) > distance:
                wins += 1
        res *= wins

    return res

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(solve(input))
    print(solve(input.replace(' ', '')))