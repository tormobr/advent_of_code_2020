from operator import mul, add
import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

operators = {
    "+": add,
    "*": mul
}

# Calculates expression such as 1 + 2 or 4 * 5 and returns the answer
def sum_add(m):
    a = int(m["a"])
    b = int(m["b"])
    op = operators[m["op"]]

    return str(op(a, b))

# Caclulates the expression inside paranthesis for part 1
def calculate_inside(m):
    while "+" in m or "*" in m:
        m = re.sub("^(?P<a>\d+)\s+(?P<op>.)\s+(?P<b>\d+)", sum_add, m)
    return m

# Caclulates the expression inside paranthesis for part 2
def calculate_inside_2(m):
    while "+" in m:
        m = re.sub("(?P<a>\d+)\s+(?P<op>\+)\s+(?P<b>\d+)", sum_add, m)
    while "*" in m:
        m = re.sub("(?P<a>\d+)\s+(?P<op>\*)\s+(?P<b>\d+)", sum_add, m)

    return m

# iterates over the expression until there are no more paranthesis left
def iterate(s, f=calculate_inside):
    inner_par = re.compile(r"\((?P<exp>[^()]+)\)")
    while "(" in s:
        s = re.sub(inner_par, lambda m: f(m["exp"]), s)

    return int(f(s))
    

# Part 1 solution : 
def part_1():
    data = read_lines("input.txt", f=str)
    return sum(iterate(s) for s in data)

# Part 2 solution : 
def part_2():
    data = read_lines("input.txt", f=str)
    return sum(iterate(s, f=calculate_inside_2) for s in data)

if __name__ == "__main__":
    pretty_print(part_1(), part_2())

