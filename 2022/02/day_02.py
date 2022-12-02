from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
from itertools import combinations

sample = '''\
A Y
B X
C Z
'''

def get_score_1(line):
    def get_outcome(shape1, shape2):
        if shape1 == 'rock' and shape2 == 'rock':
            return 3
        elif shape1 == 'rock' and shape2 == 'paper':
            return 6
        elif shape1 == 'rock' and shape2 == 'scissors':
            return 0
        elif shape1 == 'paper' and shape2 == 'rock':
            return 0
        elif shape1 == 'paper' and shape2 == 'paper':
            return 3
        elif shape1 == 'paper' and shape2 == 'scissors':
            return 6
        elif shape1 == 'scissors' and shape2 == 'rock':
            return 6
        elif shape1 == 'scissors' and shape2 == 'paper':
            return 0
        elif shape1 == 'scissors' and shape2 == 'scissors':
            return 3

    def get_shape(shape):
        if shape in ['A', 'X']:
            return 'rock'
        elif shape in ['B', 'Y']:
            return 'paper'
        elif shape in ['C', 'Z']:
            return 'scissors'

    shape1, shape2 = line.split()
    return (['X', 'Y', 'Z']).index(shape2) + 1 + get_outcome(get_shape(shape1), get_shape(shape2))

def get_score_2(line):
    shape1, outcome = line.split()
    shape1 = ['rock', 'paper', 'scissors'][['A', 'B', 'C'].index(shape1)]
    outcome = ['lose', 'draw', 'win'][['X', 'Y', 'Z'].index(outcome)]

    def get_my_shape(shape1, outcome):
        if outcome == 'draw':
            return shape1
        elif shape1 == 'rock' and outcome == 'win':
            return 'paper'
        elif shape1 == 'rock' and outcome == 'lose':
            return 'scissors'
        elif shape1 == 'paper' and outcome == 'win':
            return 'scissors'
        elif shape1 == 'paper' and outcome == 'lose':
            return 'rock'
        elif shape1 == 'scissors' and outcome == 'win':
            return 'rock'
        elif shape1 == 'scissors' and outcome == 'lose':
            return 'paper'

    def get_my_shape_value(shape):
        return ['rock', 'paper', 'scissors'].index(shape) + 1

    return get_my_shape_value(get_my_shape(shape1, outcome)) + ['lose', 'draw', 'win'].index(outcome) * 3

def part_1(input):
    return sum([get_score_1(line) for line in input.splitlines()])

def part_2(input):
    return sum([get_score_2(line) for line in input.splitlines()])

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))
