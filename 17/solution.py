from collections import deque, defaultdict
import itertools

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    grid = read_lines_sep("input.txt", sep="", f=str)
    dim = len(grid) 
    
    locs = defaultdict(lambda: ".")
    for y, row in enumerate(grid):
        for x, elem in enumerate(row):
            locs[(0, y, x)] = elem

    dirs = list(itertools.product([0,1,-1], repeat=3))
    dirs.remove((0,0,0))
    for its in range(6):
        new_locs = locs.copy()
        for z in range((its+1)*-1, its+2):
            for y in range((its+1)*-1, its+dim+2):
                for x in range((its+1)*-1, its+dim+2):
                    elem = locs[(z, y, x)]
                    c = 0
                    for dx, dy, dz in dirs:
                        new_x = x + dx
                        new_y = y + dy
                        new_z = z + dz
                        if (new_z, new_y, new_x) not in locs.keys():
                            continue
                        if locs[(new_z, new_y, new_x)] == "#":
                            c += 1

                    if elem == "#" and c not in [2,3]:
                        new_locs[(z, y, x)]  = "."

                    elif c == 3 and elem == ".":
                        new_locs[(z, y, x)]  = "#"
        locs = new_locs

    return sum(value == "#" for value in locs.values())

# Part 2 solution : 
def part_2():
    grid = read_lines_sep("input.txt", sep="", f=str)
    dim = len(grid)
    

    locs = defaultdict(lambda: ".")
    for y, row in enumerate(grid):
        for x, elem in enumerate(row):
            locs[(0, 0, y, x)] = elem

      
    dirs = list(itertools.product([0,1,-1], repeat=4))
    dirs.remove((0,0,0,0))
    for its in range(6):
        new_locs = locs.copy()
        #print(new_locs)
        for w in range((its+1)*-1, its+2):
            for z in range((its+1)*-1, its+2):
                for y in range((its+1)*-1, its+dim+2):
                    for x in range((its+1)*-1, its+dim+2):
                        c = 0
                        for dw, dx, dy, dz in dirs:
                            new_x = x + dx
                            new_y = y + dy
                            new_z = z + dz
                            new_w = w + dw

                            if locs[(new_w, new_z, new_y, new_x)] == "#":
                                c += 1

                        if locs[(w,z,y,x)] == "#" and c not in [2,3]:
                            new_locs[(w, z, y, x)]  = "."

                        elif c == 3 and locs[(w,z,y,x)] == ".":
                            new_locs[(w, z, y, x)]  = "#"
        locs = new_locs

    return sum(value == "#" for value in locs.values())

if __name__ == "__main__":
    pretty_print(part_1(), part_2())
