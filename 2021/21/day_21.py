from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms
from collections import defaultdict

sample = '''\
Player 1 starting position: 4
Player 2 starting position: 8
'''

ROLL_COUNT = 0

def dice():
    global ROLL_COUNT
    while True:
        for i in range(100):
            ROLL_COUNT += 1
            yield i + 1

@measure_ms
def part_1(input):
    lines = input.splitlines()
    pos1 = int(lines[0][-1]) - 1
    pos2 = int(lines[1][-1]) - 1
    score1, score2 = 0, 0
    roll = dice()
    while True:
        pos1 = (pos1 + next(roll) + next(roll) + next(roll)) % 10
        score1 += pos1 + 1
        if score1 >= 1000:
            return ROLL_COUNT * score2
        pos2 = (pos2 + next(roll) + next(roll) + next(roll)) % 10
        score2 += pos2 + 1
        if score2 >= 1000:
            return ROLL_COUNT * score1

@measure_ms
def part_2(input):
    rolls = defaultdict(int)
    lines = input.splitlines()
    pos1 = int(lines[0][-1]) - 1
    pos2 = int(lines[1][-1]) - 1
    U = defaultdict(int)
    U[(pos1, pos2, 0, 0)] = 1
    win_count1, win_count2 = 0, 0

    for r1 in range(2):
        for r2 in range(2):
            for r3 in range(2):
                rolls[r1 + r2 + r3 + 3] += 1

    while len(U) > 0:
        N = defaultdict(int)
        for u_conf, u_count in U.items():
            for roll_value, roll_count in rolls.items():
                pos, score = u_conf[0], u_conf[2]
                pos = (pos + roll_value) % 10
                score += pos + 1
                if score >= 21:
                    win_count1 += u_count * roll_count
                else:
                    N[(pos, u_conf[1], score, u_conf[3])] = u_count * roll_count
        U = N
        N = defaultdict(int)
        for u_conf, u_count in U.items():
            for roll_value, roll_count in rolls.items():
                pos, score = u_conf[1], u_conf[3]
                pos = (pos + roll_value) % 10
                score += pos + 1
                if score >= 21:
                    win_count2 += u_count * roll_count
                else:
                    N[(u_conf[0], pos, u_conf[2], score)] = u_count * roll_count
        U = N
            
    return win_count1, win_count2

if __name__ == '__main__':
    input = get_input()
    input = sample
    print(part_1(input))
    print(part_2(input))      
