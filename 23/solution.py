import sys
sys.path.insert(0,'..')
from advent_lib import *

# Node class to represent values from input data
class Node():
    def __init__(self, v):
        self.next = None
        self.v = v
    def __str__(self):
        return f"v: {self.v}"
    def __repr__(self):
        return self.__str__()

# Gets the correct destination node
def get_dst(x, data, pick):
    curr = x -1
    while True:
        if curr == 0:
            curr = len(data)
        if curr not in [p.v for p in pick]:
            return curr
        curr -= 1


# playes the game with crab and return nodes after done
def solve(p2=False):
    data = read_lines_sep("input.txt", f=int, sep="")[0]
    # Appends
    if p2:
        data.extend(range(len(data)+1, 1000001))

    # Create node data structiure
    nodes = {v:Node(v) for v in data}
    for i in range(len(data)):
        nodes[data[i]].next = nodes[data[(i+1) % len(data)]]

    # Set inital values
    its = 10000000 if p2 else 100
    current = nodes[data[0]]
    for it in range(its):
        # Get the next 3 nodes
        a, b, c = current.next, current.next.next, current.next.next.next
        pick = [a, b, c]

        # find the correct node to insert at
        dst = get_dst(current.v, data, pick)
        dst = nodes[dst]

        # Update next pointers for next iteration
        current.next = c.next
        current = c.next
        c.next = dst.next
        dst.next = a

    return nodes

# Solves part 1
def part_1():
    nodes = solve()
    curr = nodes[1].next
    res = ""
    for i in range(len(nodes)-1):
        res += str(curr.v)
        curr = curr.next
    return res

# Solves part 2 
def part_2():
    nodes = solve(p2=True)
    a = nodes[1].next
    b = a.next
    return a.v * b.v

if __name__ == "__main__":
    pretty_print(part_1(), part_2())
