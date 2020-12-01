from operator import mul

def read_lines(f):
    return [f(l.strip()) for l in open("input.txt")]


def part1():
    numbers = read_lines(int)
    for n in numbers:
        for n2 in numbers:
            if n + n2 == 2020:
                return n * n2

def part2():
    numbers = read_lines(int)
    for n in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if n + n2 + n3 == 2020:
                    return n * n2 * n3

if __name__ == "__main__":
    print(part1())
    print(part2())
