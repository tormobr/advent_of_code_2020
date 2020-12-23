import sys
sys.path.insert(0,'..')
from advent_lib import *

def solve(t=2020):
    data = read_sep("input.txt", sep=",", f=int)

    d = {}
    for i, n in enumerate(data):
        d[n] = (i, i)
    
    SEEN = set(d.keys())
    last = data[-1]
    turn = len(data)
    while True:
        a, b = d[last]
        if turn == t:
            return last
        #print("last num: ", last)
        #print(a,b)
        last = b - a 

        if last not in SEEN:
            d[last] = (turn, turn)
        else:
            d[last] = (d[last][1], turn)
        
        SEEN.add(last)
        turn += 1


    print(d)

    return None

# Part 1 solution : 
def part_1():
    return solve()

# Part 2 solution : 
def part_2():
    return solve(t=30000000)


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
