from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce\
'''

def part_1(input):
    res = 0
    for line in input.split('\n'):
        output = line.split('|')[1]
        for o in output.strip().split(' '):
            if len(o) in [7, 4, 2, 3]:
                res += 1
    return res

def part_2(input):
    res = 0
    for line in input.split('\n'):
        pattern, digit = [], []
        output = line.split('|')[0]
        for o in output.strip().split(' '):
            pattern.append(''.join(sorted(o)))
        output = line.split('|')[1]
        for o in output.strip().split(' '):
            digit.append(''.join(sorted(o)))

#  _   _   _   len == 5, 3 contains both from _one_
#  _|  _| |_             5 contains both from _four_
# |_   _|  _|            2 else
#  _   _   _   len == 6, 6 contains only one from _one_
# | | |_  |_|            9 contains both from _four_
# |_| |_|  _|            0 else
#          _   _
#   | |_|   | |_|
#   |   |   | |_|

        one = ''    
        four = ''
        P = {}
        for p in pattern:
            if len(p) == 2:
                P[p] = '1'
                one = p
            if len(p) == 4:
                P[p] = '4'
                f = p
            if len(p) == 3:
                P[p] = '7'
            if len(p) == 7:
                P[p] = '8'
        for ch in f:
            if not ch in one:
                four += ch
        for p in pattern:
            if len(p) == 5:
                if (one[0] in p) and (one[1] in p):
                    P[p] = '3'
                elif (four[0] in p) and (four[1] in p):
                    P[p] = '5'
                else:
                    P[p] = '2'
            if len(p) == 6:
                if ((one[0] in p) and (not (one[1] in p))) or (not (one[0] in p) and (one[1] in p)):
                    P[p] = '6'
                elif (four[0] in p) and (four[1] in p):
                    P[p] = '9'
                else:
                    P[p] = '0'
        num = ''
        for d in digit:
            num += P[d]
        res += int(num)

    return res

if __name__ == '__main__':
    input  = get_input()
    # print(part_1(sample))
    print(part_1(input))
    # print(part_2('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'))
    # print(part_2(sample))
    print(part_2(input))      
