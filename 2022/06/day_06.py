from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

def part_1(input):
    res = 0
    while input:
        if len(set([input[res], input[res + 1], input[res + 2], input[res + 3]])) == 4:
            return res + 4
        res += 1 

def part_2(input, ln):
    res = 0
    input = [ch for ch in input]
    word = []
    for _ in range(ln):
        word.append(input.pop(0))
        res += 1
    while True:
        if len(set(word)) == ln:
            return res
        word.pop(0)
        word.append(input.pop(0))
        res += 1

if __name__ == '__main__':
    input = get_input()
    assert part_1('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
    assert part_1('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert part_1('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert part_1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert part_1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
    print(part_1(input))
    assert part_2('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
    assert part_2('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
    assert part_2('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
    assert part_2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
    assert part_2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26
    print(part_2(input, 14))
