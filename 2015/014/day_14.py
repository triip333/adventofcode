from os import sys, path
import re
from collections import defaultdict
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.\
'''

def part_1(input, n):
    res = 0
    for line in input.strip().splitlines():
        speed, time, stop = [int(x) for x in re.findall('\d+', line)]
        laps = n // (time + stop)
        remaining = n % (time + stop)
        res = max(res, speed * time * laps + speed * min(remaining, time))
    return res

def part_2(input, n):
    reindeer = {}
    distance = defaultdict(int)
    score = defaultdict(int)
    for line in input.strip().splitlines():
        name = line.split()[0]
        speed, time, stop = [int(x) for x in re.findall('\d+', line)]
        reindeer[name] = speed, time, stop
    for i in range(n):
        for name in reindeer.keys():
            speed, time, stop = reindeer[name]
            if (i % (time + stop)) in range(time):
                distance[name] += speed
        best = max(distance.values())
        for name in reindeer.keys():
            if distance[name] == best:
                score[name] += 1

    return max(score.values())

if __name__ == '__main__':
    input, duration = get_input(), 2503
    # input, duration = sample, 1000
    print(part_1(input, duration))
    print(part_2(input, duration))
