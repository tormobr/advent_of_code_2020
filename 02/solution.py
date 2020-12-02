import re
import sys
sys.path.insert(0,'..')
from advent_lib import *


# Part 1 solution. Simply count occurences of letter in string
def part_1():
    s = re.sub(r" |-|:", " ", read_string("input.txt"))
    lines = read_lines_sep(s, use_file=False)
    
    return sum([p.count(l) in range(int(s), int(e)+1) for s,e,l,p in lines])

# Part 2. if letter apears on only one of the indexes it's valid
def part_2():
    s = re.sub(r" |-|:", " ", read_string("input.txt"))
    lines = read_lines_sep(s, use_file=False)

    return sum([(p[int(s)-1]==l) ^ (p[int(e)-1]==l) for s,e,l,p in lines])


if __name__ == "__main__":
    print(f"\n{WARNING}RESULTS:\n------------------------------------{ENDC}")
    print(f"{HEADER}Part 1: {OKGREEN} {part_1()}{ENDC}")
    print(f"{HEADER}Part 2: {OKGREEN} {part_2()}{ENDC}")
    print(f"{WARNING}------------------------------------\n{ENDC}")
