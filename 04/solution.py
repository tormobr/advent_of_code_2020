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
    glob = []
    with open("input.txt") as f:
        current = ""
        for line in f:
            if line == "\n":
                hax = re.split(r" |\n", current)[:-1]
                print("new _ password")
                tmp = {}
                for item in hax:
                    print(item)
                    key = item.split(":")[0]
                    val = item.split(":")[1]

                    tmp[key] = val
                
                glob.append(tmp)
                current = ""
                print("done adding one\n")
                continue
            current += str(re.sub("\n", " ", line))
            #print(current)
            

    ret = 0
    for item in glob:
        if len(item) < 7:
            continue
        if len(item) == 7 and "cid" in item.keys():
            continue
        print(len(item))
        if (int(item["byr"]) <= 2002 and int(item["byr"]) >= 1920) and (int(item["iyr"]) <= 2020 and int(item["iyr"]) >= 2010) and (int(item["eyr"]) <= 2030 and int(item["eyr"]) >= 2020) and (re.match(r"^#[\d|a-f]{6}$", item["hcl"])) and (item["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) and (re.match("^\d{9}$", item["pid"])): 

            if "cm" in item["hgt"]:
                s = int(item["hgt"].replace("cm", ""))
                if s >= 150 and s <= 193:
                    ret += 1
            elif "in" in item["hgt"]:
                s = int(item["hgt"].replace("in", ""))
                if s >= 59 and s <= 76:
                    ret += 1
            else:
                print(item)
        else:
            print(item)

    return ret

# Part 2 solution : 
def part_2():
    return None


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
