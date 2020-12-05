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

# Part 1 solution : 
def part_1():
    data = read_lines("input.txt", f=int)
    data = read_string("input.txt")
    data = read_sep("input.txt", sep=",", f=int)
    data = read_lines_sep("input.txt", sep=",", f=str)

    print_arr(data)

    for y, row in enumerate(data):
        for x, elem in enumerate(row):
            pass

    return None

# Part 2 solution : 
def part_2():
    return None


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
