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

sys.setrecursionlimit(100000)

def flip_rot(grid, ID=None):
    ret = []
    for _ in range(4):
        grid = np.rot90(grid)
        if ID:
            ret.append((ID, deepcopy(grid)))
        else:
            ret.append(deepcopy(grid))
    grid = grid[::-1]
    for _ in range(4):
        grid = np.rot90(grid)
        if ID:
            ret.append((ID, deepcopy(grid)))
        else:
            ret.append(deepcopy(grid))
    return ret

def strip_grid(grid):
    return grid[1:-1, 1:-1]

def check_match(x, y, fill):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    curr = fill[y][x]
    grids = [[] for _ in range(4)]
    for i, (dx, dy) in enumerate(dirs):
        new_x = dx + x
        new_y = dy + y
        if new_x < 0 or new_x > len(fill)-1:
            continue
        if new_y < 0 or new_y > len(fill)-1:
            continue
        new_grid = fill[new_y][new_x]
        grids[i] = new_grid
    
    right, down, left, up = grids[0], grids[1], grids[2], grids[3]
    if len(up) > 0 and not np.all(curr[0] == up[-1]):
        return False
    if len(down) > 0 and not np.all(curr[-1] == down[0]):
        return False
    if len(left) > 0 and not np.all(curr[:,0] == left[:,-1]):
        return False
    if len(right) > 0 and not np.all(curr[:,-1] == right[:,0]):
        return False
    return True

def stitch_grids(grid_list):
    grids = [[strip_grid(g) for g in row] for row in grid_list]
    hor = np.array([np.vstack([g for g in grids[i]]) for i in range(len(grids))])
    vert = np.hstack(hor)
    return vert

# Part 1 solution : 
def part_1():
    D = {}
    for tile in open("input.txt").read().split("\n\n"):
        lines = tile.strip().split("\n")
        ID = ints(lines[0])[0]
        D[ID] = np.array([[x.strip() for x in line] for line in lines[1:]])

    # Create data structures
    sq = int(math.sqrt(len(D.keys())))
    fill = [[[] for x in range (sq)] for row in range(sq)]
    fill_ID = [[None]*sq for row in range(sq)]

    # Generate possible rotations and flips of all grids
    possible = []
    for ID, grid in D.items():
        possible.extend(flip_rot(grid, ID))

    SEEN = set()
    combs = []
    grid_combs = []
    def rec(current, ID, x, y):
        if combs:
            return True
        if ID in SEEN:
            return False
        SEEN.add(ID)
        fill[y][x] = deepcopy(current)
        fill_ID[y][x] = ID
        #print("new rec!", x, y, fill_ID)
        #time.sleep(.9)
        if x == len(fill) -1 and y == len(fill)-1:
            combs.append(deepcopy(fill_ID))
            grid_combs.append(deepcopy(fill))
            print("appending to res")
            time.sleep(1)
            fill[y][x] = []
            fill_ID[y][x] = None
            return True

        if not check_match(x, y, fill):
            SEEN.remove(ID)
            fill[y][x] = []
            fill_ID[y][x] = None
            return False

        hax = False
        for new_ID, n in possible:
            if combs:
                return True
            if new_ID in SEEN:
                continue
            if x == len(fill)-1:
                new_x = 0
                new_y = y+1
            else:
                new_x = x+1
                new_y =  y
            ret = rec(n, new_ID,  new_x, new_y)
            if ret:
                hax = True

        if ID in SEEN:
            SEEN.remove(ID)
        fill[y][x] = []
        fill_ID[y][x] = None
        return hax
    

        
    # Call recursive functions starting at every possible tile variant
    for i, (ID, p) in enumerate(possible):
        SEEN = set([])
        print("calling dr love", i)
        ret = rec(p, ID, 0, 0)

    
    main_grid = stitch_grids(grid_combs[0])
    grid_combs = flip_rot(main_grid)
    #for g in grid_combs:
        #for l in g:
            #print("".join(l))
        #print("\n")
    #return
    for grid in grid_combs:
        #vert = stitch_grids(grids)
        count = count_monsters(grid)
        print("monster count: ", count)
        for row in grid:
            print("".join(row))
        print("\n")
        
        # "#" in monster = 15
        if count > 0:
            print("this happens")
            res = np.count_nonzero(grid == "#")
            return res - (count * 15 )
        
        #print(vert)
    #print(combined)


    


    return None

def count_monsters(grid):
    m1 = "                  # "
    m2 = "#    ##    ##    ###"
    m3 = " #  #  #  #  #  #   "
    monster = [list(m1), list(m2), list(m3)]
    mh = 3
    mw = len(m1)
    
    H, W = grid.shape
    c = 0
    for y, row in enumerate(grid):
        if y >= (H - mh):
            break
        for x, elem in enumerate(grid):
            if x >= (W - mw):
                break

            pot_mon = grid[y:y+mh, x:x+mw]
            found = True
            for r1, r2 in zip(monster, pot_mon):
                for e1, e2 in zip(r1, r2):
                    if e1 == " ":
                        continue
                    if e1 != e2:
                        found = False
                        break
            if found:
                print("found monster")
                c += 1

    return c

    """
    def edges(grid):
        top = grid[0]
        bottom = grid[-1]
        right = grid[:,-1]
        left = grid[:,0]
        return top, bottom, right, left

    edge_values = defaultdict(int)
    edge_names = defaultdict(list)
    id_edges = defaultdict(list)
    
    for ID,grid in D.items():
        #top, bottom, right, left = edges(grid)
        grid_edges = edges(grid)
        for e in grid_edges:
            e = tuple(min(list(e), list(e[::-1])))
            #e = tuple(e)
            edge_values[e] += 1
            edge_names[e].append(ID)
            id_edges[ID].append(e)
    
    res = 1
    for ID, edges in id_edges.items():
        hax = 0
        for e in edges:
            v = edge_values[e]
            if v == 1:
                hax += 1
        if hax == 2:
            print("this never happens")
            res *= ID
            print(ID)
    return  res
    """
# Part 2 solution : 
def part_2():
    return None


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
