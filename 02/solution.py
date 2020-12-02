import re
import sys
sys.path.insert(0,'..')
from advent_lib import *


# Part 1 solution. Simply count occurences of letter in string
def part_1():
    s = read_string("input.txt")    # Read the string
    
    lines = re.sub(r" |-|:", " ", s).split("\n")[:-1]
    lines = [l.split() for l in lines]
    
    return sum([p.count(l) in range(int(s), int(e)+1) for s,e,l,p in lines])

# Part 2. if letter apears on only one of the indexes it's valid
def part_2():
    s = read_string("input.txt")

    lines = re.sub(r" |-|:", " ", s).split("\n")[:-1]
    lines = [l.split() for l in lines]

    return sum([(p[int(s)-1]==l) ^ (p[int(e)-1]==l) for s,e,l,p in lines])


if __name__ == "__main__":
    print(f"\n{WARNING}RESULTS:\n------------------------------------")
    print(f"{HEADER}Part 1: {OKGREEN} {part_1()}{ENDC}")
    print(f"{HEADER}Part 2: {OKGREEN} {part_2()}{ENDC}")
    print(f"{WARNING}------------------------------------\n{ENDC}")
