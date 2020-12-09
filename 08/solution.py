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

class solver:
    def __init__(self):
        self.acc = 0
        self.index = 0
        self.normal_ret = False
        self.input = self.read_input()
        self.op_funcs = {
            "acc": self.op_acc,
            "jmp": self.op_jmp,
            "nop": self.op_nop
        }

    def read_input(self, filename="input.txt"):
        return [(line.split()[0], int(line.split()[1])) for line in open(filename)]

    def op_acc(self, v):
        self.acc += v

    def op_jmp(self, v):
        self.index += v - 1

    def op_nop(self, v):
        pass



    def execute_op_codes(self, op_codes):
        # Reset the acc and the index
        self.acc = 0
        self.index = 0
        SEEN = set()
        while True:
            op_code, val = op_codes[self.index]

            if self.index >= len(op_codes) -1:
                self.normal_term = True
                break
            if self.index in SEEN:
                self.normal_term = False
                break

            SEEN.add(self.index)

            self.op_funcs[op_code](val)
            self.index += 1

    def part_1(self):
        data = self.read_input()
        self.execute_op_codes(self.input)
        return self.acc


    def part_2(self):
        data = self.read_input()
        replacements = [i for i, val in enumerate(data) if val[0] == "jmp"]
        for r in replacements:
            data[r] = ("nop", data[r][1])
            self.execute_op_codes(data)
            if self.normal_term:
                return self.acc
            data[r] = ("jmp", data[r][1])

if __name__ == "__main__":
    s = solver()
    pretty_print(s.part_1(), s.part_2())
