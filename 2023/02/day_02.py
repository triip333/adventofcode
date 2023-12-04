from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
from collections import defaultdict
import math

sample = '''\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''

def part_1(input):
    res = 0
    for line in input.splitlines():
        line = line.split(': ')
        game = line[0].split()[1]
        possible = True
        for round in line[1].split('; '):
            for grab in round.split(', '):
                amount, colour = grab.split()
                if colour == 'red' and int(amount) > 12:
                    possible = False
                elif colour == 'green' and int(amount) > 13:
                    possible = False
                elif colour == 'blue' and int(amount) > 14:
                    possible = False
        if possible:
            res += int(game)
    return res


def part_2(input):
    res = 0
    for line in input.splitlines():
        d = defaultdict(int)
        line = line.split(': ')
        for round in line[1].split('; '):
            for grab in round.split(', '):
                amount, colour = grab.split()
                d[colour] = max(int(amount), d[colour])
        res += math.prod(d.values())
    return res

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))
