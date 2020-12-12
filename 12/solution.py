from copy import deepcopy
import math
from collections import deque, defaultdict, Counter
from functools import reduce
from operator import mul
import itertools
import numpy as np
import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

DIRECTIONS = {
    "E": (0, 1),
    "W": (0, -1),
    "S": (1, 0),
    "N": (-1, 0)
}

SPIN_DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# Part 1 solution : 
def part_1():
    data = read_lines("input.txt", f=str)
    hax = []
    for line in data:
        command = line[0]
        num = int(line[1:])
        hax.append((command, num))
    print_arr(hax)
    

    pos_x = 0
    pos_y = 0
    face_index = 0
    new_dir = (0, 1)
    for com, num in hax:
        if com == "F":
            
            new_dir = SPIN_DIRS[face_index % 4]
            
            current_y, current_x = new_dir
            pos_x += num*current_x
            pos_y += num*current_y
            #print("moving: ", new_dir, num, "current: ", pos_y, pos_x)
            continue
        elif com == "R":
            face_index += num // 90
            continue
        elif com == "L":
            face_index -= num // 90
            continue

        new_dir = DIRECTIONS[com]
        
        current_y, current_x = new_dir
        pos_x += num*current_x
        pos_y += num*current_y
        #print("com: ", com, new_dir, num, "current: ", pos_x, pos_y)

    return abs(pos_x) + abs(pos_y)



    return None

# Part 2 solution : 
def part_2():
    data = read_lines("input.txt", f=str)
    hax = []
    for line in data:
        command = line[0]
        num = int(line[1:])
        hax.append((command, num))
    print_arr(hax)
    

    pos_x = 0
    pos_y = 0
    way_x = 10
    way_y = -1
    face_index = 0
    new_dir = (0, 1)
    for com, num in hax:
        if com == "F":
            pos_x += num*way_x
            pos_y += num*way_y
            print("moving ship: ", num, "current: ", pos_x, pos_y)
            continue
        elif com == "R":
            spin = num // 90
            for i in range(spin):
                way_x, way_y = -way_y, way_x
                print("rorated waypoint: ", way_x, way_y)
            continue
        # SPIN_DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # R90: (-4, 10) => (10, 4)
        elif com == "L":
            spin = num // 90
            for i in range(spin):
                way_x, way_y = way_y, -way_x
                print("rorated waypoint: ", way_x, way_y)
            continue

        new_dir = DIRECTIONS[com]
        
        dir_y, dir_x = new_dir
        way_x += num*dir_x
        way_y += num*dir_y
        print("movin waypoint: ", way_x, way_y)

    return abs(pos_x) + abs(pos_y)


if __name__ == "__main__":
    pretty_print(part_1(), None)
