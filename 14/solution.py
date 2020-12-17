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

def apply_mask(s, MASK):
    res = ""
    for a, b in zip(s, MASK):
        if b == "X":
            res += a
        else:
            res += b
    return int(res, 2)

def part_1():
    addr = {}
    s = open("input.txt").read().strip()
    s = re.sub(r" = ", r"=", s)
    MEM = {}
    MASK = ""
    for line in s.split("\n"):
        k, v = line.strip().split("=")
        if "mask" in k:
            MASK = v
        elif "mem" in k:
            addr, value = ints(line)
            bitstring = "{0:036b}".format(value)
            masked_value = apply_mask(bitstring, MASK)
            MEM[addr] = masked_value
    res = 0
    for k, v in MEM.items():
        res += v
    return res

def apply_mask_2(s, MASK):
    res = ""
    perms = 0
    for a, b in zip(s, MASK):
        if b == "X":
            res += "X"
            perms += 1
        elif b == "0":
            res += a
        elif b == "1":
            res += b
    
    prod = list(itertools.product([1, 0], repeat=perms))
    hax = []
    for p in prod:
        index = 0
        new_addr = ""
        for c in res:
            if c == "X":
                new_addr += str(p[index])
                index += 1
            else:
                new_addr += c
        hax.append(int(new_addr, 2))
    return hax


# Part 2 solution : 
def part_2():
    addr = {}
    s = open("input.txt").read().strip()
    s = re.sub(r" = ", r"=", s)
    MEM = {}
    MASK = ""
    for line in s.split("\n"):
        k, v = line.strip().split("=")
        if "mask" in k:
            MASK = v
        elif "mem" in k:
            addr, value = ints(line)
            bitstring = "{0:036b}".format(addr)
            masked_addr = apply_mask_2(bitstring, MASK)
            for a in masked_addr:
                MEM[a] = value
    res = 0
    for k, v in MEM.items():
        res += v
    return res


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
