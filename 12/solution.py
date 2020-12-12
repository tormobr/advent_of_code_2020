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
    data = [(line[0], int(line[1:])) for line in open("input.txt")]

    pos_x, pos_y = 0, 0
    face_index = 0
    for command, num in data:
        if command == "F":
            dir_y, dir_x = SPIN_DIRS[face_index % 4]
            pos_x += num*dir_x
            pos_y += num*dir_y
            
        elif command == "R":
            face_index += num // 90

        elif command == "L":
            face_index -= num // 90

        else:
            dir_y, dir_x = DIRECTIONS[command]
            pos_x += num*dir_x
            pos_y += num*dir_y

    return abs(pos_x) + abs(pos_y)



    return None

# Part 2 solution : 
def part_2():
    data = [(line[0], int(line[1:])) for line in open("input.txt")]

    pos_x, pos_y = 0, 0
    way_x, way_y = 10, -1
    for command, num in data:
        if command == "F":
            pos_x += num*way_x
            pos_y += num*way_y

        elif command == "R":
            rotations = num // 90
            for _ in range(rotations):
                way_x, way_y = -way_y, way_x

        elif command == "L":
            rotations = num // 90
            for _ in range(rotations):
                way_x, way_y = way_y, -way_x
        else:
            dir_y, dir_x  = DIRECTIONS[command]
            way_x += num*dir_x
            way_y += num*dir_y

    return abs(pos_x) + abs(pos_y)


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
