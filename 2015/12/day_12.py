from os import sys, path
import re, json

from numpy import isin
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
{"d":"red","e":[1,2,3,4],"f":5}\
'''

def part_1(input):
    return sum([int(r) for r in re.findall('-?\d+', input.strip())])

def get_sum(val):
    res = 0

    if isinstance(val, list):
        for v in val:
            res += get_sum(v)
    elif isinstance(val, dict):
        if not 'red' in val.values():
            for v in val.values():
                res += get_sum(v)
    elif isinstance(val, int):
        res += int(val)
            
    return res

def part_2(input):
    return get_sum(json.loads(input))

if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(part_1(input))
    print(part_2(input))