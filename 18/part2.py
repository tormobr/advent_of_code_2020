
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
        ops = []
        nums = []
        #for j, curr in enumerate(hax[index:]):
        while index < len(hax):
            curr = hax[index]
            print(index, curr)
            if curr == "(":
                res, skip = rec(index+1, hax)
                nums.append(res)
                print("exit rec: ", nums)
                index = skip

            # 1 * 2 * 3 + 4
            # [1,2,3, 4]
            # [*, *, +]
            elif curr == ")" or index >= len(hax):
                print("HAX")
                print(nums)
                print(ops)
                i = 0
                while add in ops:
                    print(ops)
                    print(nums)
                    op = ops[i]
                    if op == add:
                        print("this happens")
                        a = nums.pop(i)
                        b = nums.pop(i)
                        nums.insert(i, add(a, b))
                        ops.pop(i)
                        continue
                    i += 1
                i = 0
                while mul in ops:
                    print(ops)
                    print(nums)
                    op = ops[i]
                    if op == mul:
                        a = nums.pop(i)
                        b = nums.pop(i)
                        nums.insert(i, mul(a, b))
                        ops.pop(i)
                        continue
                    i += 1
                print("ASNANSDNASNDNASNDAS_:", nums[0])
                return nums[0], index

            elif curr in ["+", "-", "*", "/"]:
                ops.append(directions[curr])

            else:       # number
                nums.append(int(curr))
            index += 1
        print("HAX")
        print(nums)
        print(ops)
        i = 0
        while add in ops:
            print(ops)
            op = ops[i]
            if op == add:
                print("this happens")
                a = nums.pop(i)
                b = nums.pop(i)
                nums.insert(i, add(a, b))
                ops.pop(i)
                continue
            i += 1
        i = 0
        while mul in ops:
            op = ops[i]
            if op == mul:
                a = nums.pop(i)
                b = nums.pop(i)
                nums.insert(i, mul(a, b))
                ops.pop(i)
                continue
            i += 1
        print("HAX")
        print(nums)
        print(ops)
        return nums[0], 1000

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
