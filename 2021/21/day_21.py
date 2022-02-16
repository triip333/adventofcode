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
    U = {}
    def get_win_count(pos1, pos2, score1, score2):
        if (pos1, pos2, score1, score2) in U:
            return U[(pos1, pos2, score1, score2)]
        else:
            res1, res2 = 0, 0
            for r1_1 in range(3):
                for r1_2 in range(3):
                    for r1_3 in range(3):
                        new_pos1 = (pos1 + r1_1 + r1_2 + r1_3 + 3) % 10
                        new_score1 = score1 + new_pos1 + 1
                        if new_score1 >= 21:
                            res1 += 1
                        else:
                            for r2_1 in range(3):
                                for r2_2 in range(3):
                                    for r2_3 in range(3):
                                        new_pos2 = (pos2 + r2_1 + r2_2 + r2_3 + 3) % 10
                                        new_score2 = score2 + new_pos2 + 1
                                        if new_score2 >= 21:
                                            res2 += 1
                                        else:
                                            s1, s2 = get_win_count( new_pos1, new_pos2, new_score1, new_score2)
                                            res1 += s1
                                            res2 += s2
            U[(pos1, pos2, score1, score2)] = res1, res2
            return res1, res2
           
    lines = input.splitlines()
    return max(get_win_count(int(lines[0][-1]) - 1, int(lines[1][-1]) - 1, 0, 0))

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))      
