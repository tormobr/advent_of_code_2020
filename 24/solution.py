from copy import deepcopy
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

dirs = {
    "e": (1, 0),
    "se": (0, 1),
    "ne": (1, -1),
    "w": (-1, 0),
    "sw": (-1, 1),
    "nw": (0, -1),
}
# Part 1 solution : 
def part_1():
    data = read_lines("input.txt", f=str)
    d = defaultdict(int)
    for s in data:
        x, y = 0, 0
        current = ""
        for c in s:
            current += c
            if current in dirs.keys():
                print(current)
                dy, dx = dirs[current]
                x += dx
                y += dy
                current = ""
        d[(y, x)] += 1
            
    return sum(v for v in d.values() if v % 2 == 1)

# Part 2 solution : 
def part_2():
    data = read_lines("input.txt", f=str)
    d = defaultdict(int)
    for s in data:
        x, y = 0, 0
        current = ""
        for c in s:
            current += c
            if current in dirs.keys():
                dy, dx = dirs[current]
                x += dx
                y += dy
                current = ""
        d[(y, x)] += 1
            
    DD = defaultdict(int)
    for k, v in d.items():
        if v % 2 == 1:
            DD[k] = 1
        else:
            DD[k] = 0

    days = 0
    for t in range(100):
        print(t, sum(v for v in DD.values()))
        new_tiles = deepcopy(DD)
        for y in range(-(20+t), (20+t)):
            for x in range(-(20+t), (20+t)):
                v = new_tiles[(y,x)]
                tot = 0
                for dy, dx in dirs.values():

                    k = (dy+y, dx+x)
                    v2 = DD[k]
                    if v2 == 1:
                        tot += 1
                if v == 1:
                    if tot == 0 or tot > 2:
                        new_tiles[(y,x)] = 0

                elif v == 0 and tot == 2 :
                    new_tiles[(y,x)] = 1

        DD = new_tiles
    return sum(v for v in DD.values())




    return None


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
