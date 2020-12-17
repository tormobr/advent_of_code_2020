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
    data = read_sep("input.txt", sep=",", f=int)

    d = {}
    for i, n in enumerate(data):
        d[n] = (i, i)
    
    last = data[-1]
    turn = len(data)
    while True:
        a, b = d[last]
        if turn == 2020:
            return last
        #print("last num: ", last)
        #print(a,b)
        last = b - a 

        if last not in d.keys():
            d[last] = (turn, turn)
        else:
            d[last] = (d[last][1], turn)
        turn += 1


    print(d)

    return None

# Part 2 solution : 
def part_2():
    return None


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
