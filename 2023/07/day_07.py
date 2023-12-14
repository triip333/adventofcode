from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input
from collections import defaultdict

card_value_1 = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]
card_value_2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]

sample = '''\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''


def sort_hand_1(hand):
    c_count, c_value = [], []
    res = defaultdict(int)
    for card in hand:
        res[card] += 1
        c_value.append(card_value_1.index(card))
    for _, v in sorted(res.items(), key=lambda c: c[1], reverse=True):
        c_count.append(v)
    return tuple([tuple(c_count), tuple(c_value)])


def sort_hand_2(hand):
    c_count, c_value = [], []
    res = defaultdict(int)
    for card in hand:
        res[card] += 1
        c_value.append(card_value_2.index(card))
    for k, v in sorted(res.items(), key=lambda c: c[1], reverse=True):
        if k != 'J':
            c_count.append(v)
    if 'J' in res:
        if res['J'] == 5:
            c_count = [5]
            c_value = [card_value_2.index('J')]
        else:
            c_count[0] +=  res['J']
    return tuple([tuple(c_count), tuple(c_value)])


def solve(input, sort_func):
    l, res = [], 0
    for line in input.splitlines():
        line = line.split()
        l.append((sort_func(line[0]), int(line[1])))
    for i, v in enumerate(sorted(l)):
        res += (i + 1) * v[1]
    return res

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(solve(input, sort_hand_1))
    print(solve(input, sort_hand_2))
