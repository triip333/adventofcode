from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

def three_vowels(input):
    res = 0
    for ch in 'aeiou':
        res += input.count(ch)
        if res >= 3:
            return True

def appears_twice(input):
    for c1, c2 in zip(input, input[1:]):
        if c1 == c2:
            return True

def contains_string(input):
    for c in ['ab', 'cd', 'pq', 'xy']:
        if c in input:
            return True
    return False

def is_nice_string_1(word):
    return three_vowels(word) and appears_twice(word) and not contains_string(word)

def double_pair(word):
    for c1, c2 in zip(word, word[1:]):
        if word.count(c1 + c2) > 1:
            return True

def one_letter_between(word):
    for c1, c2 in zip(word, word[2:]):
        if c1 == c2:
            return True

def is_nice_string_2(word):
    return double_pair(word) and one_letter_between(word)

def part_1(input):
    return sum(1 if is_nice_string_1(word) else 0 for word in input.split())

def part_2(input):
    return sum(1 if is_nice_string_2(word) else 0 for word in input.split())

if __name__ == '__main__':
    input = get_input()
    print(part_1(input))
    print(part_2(input))