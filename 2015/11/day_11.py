from os import sys, path
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

sample = '''\
ghijklmn\
'''

def increment(password):
    l = [ord(ch) - ord('a') for ch in password]
    l[len(l) - 1] += 1
    for i in range(len(l) - 1, 0, -1):
        if l[i] == 26:
            l[i] = 0
            l[i - 1] += 1
    return ''.join([chr(ord('a') + x) for x in l])

def validate(password):
    ok = False
    # Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    for a, b, c in zip(password[:-2], password[1:-1], password[2:]):
        if ord(a) == ord(b) - 1 == ord(c) - 2:
            ok = True
    if not ok:
        return False
    # Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    # Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            for j in range(i + 2, len(password) - 1):
                if password[j] == password[j + 1]:
                    return True

def solve(password):
    while True:
        password = increment(password)
        if validate(password):
            return password

if __name__ == '__main__':
    input = get_input()
    # input = sample
    input = solve(input)
    print(input)
    print(solve(input))