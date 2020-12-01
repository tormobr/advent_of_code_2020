
# Reads each number on each line in file and return list
def read_lines(filename, f=int):
    return [f(l.strip()) for l in open(filename)]

# Read a file as string
def read_string(filename):
    return open(filename).read()

# Reads file and splits on seperator
def read_sep(filename, sep, f=int):
    return [f(x.strip()) for x in open(filename).read().split(sep)]

# Reads each line and seperate items on line into 2D array
def read_line_sep(filename, sep, f=str):
    return [[f(s.strip()) for s in x.split(sep)] for x in open(filename)]


if __name__ == "__main__":
    print(read_lines("test_input/1.txt", int))
    print(read_string("test_input/2.txt"))
    print(read_sep("test_input/3.txt", ",", int))
    print(read_line_sep("test_input/4.txt", ",", str))
