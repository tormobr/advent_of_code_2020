import math
from copy import deepcopy
from collections import deque, defaultdict, Counter
from functools import reduce
from operator import mul, add, sub, truediv
import itertools
import numpy as np
import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

directions = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
}

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# Part 1 solution : 
def part_1():
    all_data = read_lines("input.txt", f=str)
    strudel = []
    for data in all_data:
        data = re.sub(r"\((:?\d)", r"( \1", data)
        data = re.sub(r"(:?\d)\)", r"\1 )", data)
        print(data)
        data = data.split()

        s = ""
        hax = []
        for c in data:
            if "(" in c:
                for _ in range(len(c)):
                    hax.append("(")
            elif ")" in c:
                for _ in range(len(c)):
                    hax.append(")")
            else:
                hax.append(c)
        strudel.append(hax)


    def rec(index, hax):
        print("new recursion")
        curr_num = None
        curr_op = None
        #for j, curr in enumerate(hax[index:]):
        while index < len(hax):
            curr = hax[index]
            print(index, curr)
            if curr == "(":
                res, skip = rec(index+1, hax)
                print("rec op", curr_op, curr_num, res)
                if curr_num:
                    curr_num = curr_op(curr_num, res)
                else:
                    curr_num = res
                index = skip

            elif curr == ")":
                return curr_num, index

            elif curr in ["+", "-", "*", "/"]:
                curr_op = directions[curr]
            else:       # number
                if not curr_num: 
                    curr_num = int(curr)
                    print("setting curr_num: ", curr_num)
                else:
                    print("norm op:", curr_op, curr_num, curr)
                    curr_num = curr_op(curr_num, int(curr))
            index += 1
        return curr_num, 1000


    res = 0
    for s in strudel:
        ret,_ = rec(0, s)
        res += ret
    return res

# Part 2 solution : 
def part_2():
    return None


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
