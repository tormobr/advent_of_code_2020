from numba import njit
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
    data = read_lines("input.txt", f=str)
    arival = int(data[0])
    busses = [int(s) for s in data[1].split(",") if s != "x"]
    new_busses = [0 for _ in range(len(busses))]
    res = []
    SEEN = set()
    while True:
        #print(new_busses)
        for i, (og_buss, new_buss) in enumerate(zip(busses, new_busses)):
            new_busses[i] = new_buss + og_buss
            if new_busses[i] >= arival and og_buss not in SEEN:
                SEEN.add(og_buss)
                res.append((new_busses[i], og_buss))
        if all(b >= arival for b in new_busses):
            target, ID = min(res, key=lambda x:x[0])
            return ((target- arival) * ID)
            

# Part 2 solution : 
def part_2():
    data = read_lines("input.txt", f=str)
    arival = int(data[0])
    busses = []
    for i, s in enumerate(data[1].split(",")):
        if s == "x":
            continue
        if i == 0:
            busses.append([int(s), int(s)])
        else:
            busses.append([int(s), i])

    #busses = busses[1:4]
    print(busses)
    #time.sleep(100)
    # 1068781
    @njit()
    def strudel(busses):
        its = 0
        t = 0
        skip = 1
        while True:
            correct = []
            for k,v in busses:
                if (t+v) % k == 0:
                    correct.append(abs(k))

            if len(correct) == len(busses):
                return t
                time.sleep(.1)
            elif correct:
                new_skip = 1 
                for c in correct:
                    new_skip *= c
                #new_skip = reduce(mul, correct)
                if new_skip > skip:
                    print(correct)
                    skip = new_skip
                    #time.sleep(2)
                    continue
            t += skip
            its += 1
    return strudel(np.array(busses[:]))

if __name__ == "__main__":
    pretty_print(part_1(), part_2())
