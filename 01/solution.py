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
    pretty_print(solve(2), solve(3))
