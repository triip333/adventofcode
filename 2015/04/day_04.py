from os import sys, path
import time
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input, measure_ms
from hashlib import md5

@measure_ms
def solve(input, n):
    for i in range(int(1e9)):
        if md5((input + str(i)).encode('utf-8')).hexdigest().startswith('0' * n):
            print(md5((input + str(i)).encode('utf-8')).hexdigest())
            return i

if __name__ == '__main__':
    input = 'iwrupvqb'
    print(solve(input, 5))
    print(solve(input, 6))
