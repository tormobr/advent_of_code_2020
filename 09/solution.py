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

    res = 0
    step = 25
    for i in range(step+1, len(data)):
        nums = data[i-step:i]
        target = data[i]
        if not any((n + n2 == target) for n, n2 in itertools.combinations(nums, 2)):
            return target

    return res


# Part 2 solution : 
def part_2():
    data = read_lines("input.txt", f=int)
    target = part_1()
    # i defines start of range
    for i, n in enumerate(data):
        current = n
        # j defines end of range
        for j, n2 in enumerate(data[i+1:]):

            # Return results if match
            if current == target:
                hax = sorted(data[i:j+i+1])
                return hax[-1] + hax[0]

            # if current sum is already over target, no need to continue
            if current > target:
                break

            current += n2


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
