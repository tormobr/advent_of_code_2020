import itertools

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    data = read_lines("input.txt", f=int)
    step = 25
    for i in range(step+1, len(data)):
        nums = data[i-step:i]
        target = data[i]
        if not any((x + y == target) for x, y in itertools.combinations(nums, 2)):
            return target

# Part 2 solution : 
def part_2():
    data = read_lines("input.txt", f=int)
    target = part_1()
    # i defines start of range
    for i, n in enumerate(data):
        current = n
        # j+i defines end of range
        for j in range(i+1, len(data)):
            current += data[j]

            # Return results if current sum match target
            if current == target:
                result_range = data[i:j]
                return min(result_range) + max(result_range)

            # if current sum is already over target, no need to continue
            if current > target:
                break



if __name__ == "__main__":
    pretty_print(part_1(), part_2())
