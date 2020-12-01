import itertools
from operator import mul
from functools import reduce
import sys
sys.path.insert(0,'..')
from advent_lib import *

# Finds all combinations and gets product of those where sum equals 2020
def solve(r):
    numbers = read_lines("input.txt", int)
    combs = itertools.combinations(numbers, r)
    return [reduce(mul, c) for c in combs if sum(c) == 2020]

if __name__ == "__main__":
    print(solve(2))
    print(solve(3))


""" Less pretty edition

def part1():
    numbers = read_lines(int)
    for n in numbers:
        for n2 in numbers:
            if n + n2 == 2020:
                return n * n2

def part2():
    numbers = read_lines(int)
    for n in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if n + n2 + n3 == 2020:
                    return n * n2 * n3

"""

