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

def extract_ids():
    data = read_lines("input.txt", f=str)
    res = []
    arrays = []
    for line in data:
        maxx = 127
        minn = 0
        max_lr = 7
        min_lr = 0
        r_count = 0
        c_count = 0
        mid_lr, mid = 0, 0
        for c in line:
            mid = (maxx + minn) // 2
            mid_lr= (max_lr + min_lr) // 2
            if c in ["B", "F"]:
                r_count += 1
                if c == "F":
                    maxx = mid
                    ret_r = minn 
                elif c == "B":
                    minn = mid
                    if mid % 2 != 0:
                        minn += 1
                    ret_r = maxx 
            elif c in ["L", "R"]:
                c_count += 1
                if c == "L":
                    max_lr= mid_lr
                    ret_lr = min_lr
                elif c == "R":
                    min_lr = mid_lr
                    if mid_lr % 2 != 0:
                        min_lr += 1
                    ret_lr = max_lr
        res.append((ret_r*8) + ret_lr)
    res.sort()
    return res
# Part 1 solution : 
def part_1():
    res = extract_ids()
    return max(res)
            

    return None

# Part 2 solution : 
def part_2():
    res = extract_ids()
    for i, ID in enumerate(res[:-1]):
        if res[i] != res[i+1] - 1:
            return ID + 1

if __name__ == "__main__":
    pretty_print(part_1(), part_2())
