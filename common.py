import os
import functools
from time import perf_counter, sleep, strftime
import urllib.request
import requests
import subprocess
import json

for file in ['conf.json', '../../conf.json']:
    if os.path.exists(file):
        with open(file) as f:
            conf = json.loads(f.read())

def get_input():
    if os.path.isfile('input'):
        with open('input') as f:
            return f.read()
    else:
        cwd = os.getcwd().split('\\')
        year = int(cwd[len(cwd) - 2])
        day = int(cwd[len(cwd) - 1])

        while True:
            h, m, s = map(int, strftime('%H %M %S').split())
            if (h >= 7) and (m >= 0) and (s >= 0):
                break
            print(f'skip {h:02}:{m:02}:{s:02}')
            sleep(1)

        input = None
        while not input:
            try:
                url = f'https://adventofcode.com/{year}/day/{day}/input'
                cookies = {'session': conf['session']}
                headers = {'User-Agent': 'python requests'}
                response = requests.get(url, cookies=cookies, headers=headers)
                input = response.text.rstrip()
                with open('input', 'w') as f:
                    f.write(input)
            except Exception as e:
                print(e)
                sleep(2)
        return input

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

def measure_s(func):
    def wrapper(*args, **kwargs):
        starttime = perf_counter()
        value = func(*args, **kwargs)
        print(f'{func.__name__} time elapsed {((perf_counter() - starttime)):.3f} s')
        return value
    return wrapper

def measure_ms(func):
    def wrapper(*args, **kwargs):
        starttime = perf_counter()
        value = func(*args, **kwargs)
        print(f'{func.__name__} time elapsed {((perf_counter() - starttime) * 1000):.3f} ms')
        return value  
    return wrapper