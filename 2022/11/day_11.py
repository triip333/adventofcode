from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_s
import operator
from functools import reduce

sample = '''\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''

class Monkey:
    def __init__(self, items, operation, divisible_by, if_true, if_false):
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.if_true = if_true
        self.if_false = if_false
        self.inspected_count = 0


def parse(input):
    res = {}
    for monkey in input.split('\n\n'):
        lines = monkey.splitlines()
        monkey_no = lines[0][:-1]
        monkey_no = monkey_no.split()[1]
        items = lines[1].split(': ')[1]
        items = [int(i) for i in items.split(', ')]
        operation = lines[2].split(': ')[1]
        assert operation.startswith('new = ')
        operation = operation.replace('new = ', '')
        test = lines[3].split(': ')[1]
        assert test.strip().startswith('divisible by'), test
        test = int(test.split()[-1])
        if_true = lines[4].split()[-1]
        if_false = lines[5].split()[-1]
        res[monkey_no] = Monkey(items, operation, test, if_true, if_false)
    return res


@measure_s
def solve(input, round_count, divided_by):
    monkeys = parse(input)
    modulo_by = reduce(operator.mul, [monkey.divisible_by for monkey in monkeys.values()])

    for i in range(round_count):
        for monkey in monkeys.values():
            while monkey.items:
                old = monkey.items.pop(0)
                monkey.inspected_count += 1
                new = eval(monkey.operation) // divided_by % modulo_by
                if new % monkey.divisible_by == 0:
                    monkeys[monkey.if_true].items.append(new)
                else:
                    monkeys[monkey.if_false].items.append(new)

    res = sorted([v.inspected_count for v in monkeys.values()])
    return res[-2] * res[-1]


if __name__ == '__main__':
    input = get_input()
    # input = sample
    print(solve(input, 20, 3))
    print(solve(input, 10000, 1))