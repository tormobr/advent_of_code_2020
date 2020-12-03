from functools import reduce
from operator import mul

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def solve(dirs):
    grid = read_lines_sep("input.txt", sep="", f=str)
    H, W = len(grid), len(grid[0])
    return reduce(mul, [sum(grid[i * dy][(i * dx) % W] == "#" for i in range(H // dy)) for dx, dy in dirs])


if __name__ == "__main__":
    pretty_print(solve([(3,1)]), solve([(1,1),(3,1),(5,1),(7,1),(1,2)]))
