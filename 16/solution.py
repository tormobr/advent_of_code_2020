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

def parse_rules(s):
    lines = s.split("\n")
    ret = {}
    for l in lines:
        l = re.sub("-", "/", l)
        v = l.split()[0]
        ret[v] = ints(l)
    return ret

def parse_near(s):
    lines = [x.split(",") for x in s.strip().split("\n")[1:]]
    return lines

        
            
def is_valid_1(ticket, rules):
    not_valids = 0
    #print("checking ticket: ", ticket)
    for x in ticket:
        x = int(x)
        found = False
        #print("Testing: ", x)
        for k, (s1,e1,s2,e2) in rules.items():
            #print("if x in range", x, s1, e1+1)
            if x in range(s1, e1+1):
                #print("match here!!!")
                found = True
            #print("if x in range", x, s2, e2+1)
            if x in range(s2, e2+1):
                #print("match here!!!")
                found = True
        if not found:
            not_valids += x
    #print(not_valids)
    return not_valids
    

def is_valid(ticket, rules):
    negs = 0 
    for x in ticket:
        x = int(x)
        found = False
        for k, (s1,e1,s2,e2) in rules.items():
            if x in range(s1, e1+1):
                found = True
            if x in range(s2, e2+1):
                found = True
        if not found:
            return False
    return True

def get_possible(ticket, rules):
    possible = [[] for _ in range(len(ticket))]
    for i, x in enumerate(ticket):
        x = int(x)
        for k, (s1,e1,s2,e2) in rules.items():
            if x in range(s1, e1+1):
                possible[i].append(k)
            if x in range(s2, e2+1):
                possible[i].append(k)
    return possible

# Part 1 solution : 
def part_1():
    rules, me, near  = open("input.txt").read().split("\n\n")

    rules = parse_rules(rules)
    near = parse_near(near)
    return (sum(is_valid_1(t, rules) for t in near))

# Part 2 solution : 
def part_2():
    rules, me, near  = open("input.txt").read().split("\n\n")

    rules = parse_rules(rules)
    near = parse_near(near)
    near = [t for t in near if is_valid_1(t, rules) == 0]
    
    me = me.split("\n")[1].split(",")
    me = [int(x) for x in me]
    #print(me)
    
    hax = []
    for t in near:
        hax.append(get_possible(t, rules))
    print(near)

    start_keys = list(rules.keys())
    res = ["" for _ in range(len(start_keys))]
    j = 0
    while True:
        if len(start_keys) == 0 or not any("departur" in s for s in start_keys):
            break
        non_valid = []
        for k in start_keys:
            if not all(k in hax[i][j] for i in range(len(near))):
                non_valid.append(k)
        print("Not valid", non_valid)
        print("current res: ", res)
        print("keys: ",start_keys)
        target = list(set(start_keys) - set(non_valid))
        if len(target) == 1:
            strudel = target[0]
            start_keys.remove(strudel)
            res[j] = strudel
        j = (j+1) % len(hax[0])
    print(res)

    ret = 1
    for x, tag in zip(me, res):
        x = int(x)
        if "departure" in tag:
            ret *= x
    return ret

if __name__ == "__main__":
    pretty_print(part_1(), part_2())
