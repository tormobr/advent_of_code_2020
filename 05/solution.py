import math
from collections import deque, defaultdict
from functools import reduce
from operator import mul
import itertools
import numpy as np
import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Gets the ids from the input data
def extract_ids():
    data = read_lines("input.txt", f=str)
    res = []
    arrays = []
    for s in data:
        row = sum([int(c=="B") << 6-i for i, c in enumerate(s[:7])])
        col = sum([int(c=="R") << 2-i for i, c in enumerate(s[7:])])
        res.append(row * 8 + col)
    res.sort()
    return res

# Part 1 solution : 
def part_1():
    res = extract_ids()
    return max(res)

# Part 2 solution : 
def part_2():
    res = extract_ids()
    for i, ID in enumerate(res[:-1]):
        if res[i] != res[i+1] - 1:
            return ID + 1

if __name__ == "__main__":
    pretty_print(part_1(), part_2())
