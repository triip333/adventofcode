from os import sys, path
import re
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

target_str = '''\
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1\
'''

def part_1(input):
    target = {}
    for line in target_str.splitlines():
        k, v = line.split(': ')
        target[k] = v

    aunts = {}
    for line in input.strip().splitlines():
        aunt = line.split(':')[0]
        aunts[aunt] = {}
        line = line[line.index(': ') + 2:]
        for l in line.split(', '):
            k, v = l.split(': ')
            aunts[aunt][k] = v
    
    while len(aunts) > 1:
        rem_list = []
        for aunt in aunts.keys():
            for k, v in aunts[aunt].items():
                if target[k] != v:
                    rem_list.append(aunt)
                    break
        for aunt in rem_list:
            del aunts[aunt]

    return aunts

def part_2(input):
    target = {}
    for line in target_str.splitlines():
        k, v = line.split(': ')
        target[k] = int(v)

    aunts = {}
    for line in input.strip().splitlines():
        aunt = line.split(':')[0]
        aunts[aunt] = {}
        line = line[line.index(': ') + 2:]
        for l in line.split(', '):
            k, v = l.split(': ')
            aunts[aunt][k] = int(v)
    
    while len(aunts) > 1:
        rem_list = []
        for aunt in aunts.keys():
            for k, v in aunts[aunt].items():
                if k in ['cats', 'trees']:
                    if target[k] >= v:
                        rem_list.append(aunt)
                        break
                elif k in ['pomeranians', 'goldfish']:
                    if target[k] <= v:
                        rem_list.append(aunt)
                        break
                elif target[k] != v:
                    rem_list.append(aunt)
                    break
        for aunt in rem_list:
            del aunts[aunt]

    return aunts

if __name__ == '__main__':
    input = get_input()
    print(part_1(input))
    print(part_2(input))
