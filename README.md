# Advent of Code
This repo contains the solutions to the problems from [advent of code](https://adventofcode.com/2020)

---

## --- Day 1: Report Repair ---
[Solution!](./01/solution.py)

### Input 
The input for this day is simply a file with integers, seperated by a newline(`\n`).

f.eks.
```
1721
979
366
299
675
1456
```

I used a list comprehension to read the lines and store the integers in an array
``` python
numbers = [int(l.strip()) for l in open("input.txt")]
```

### Part 1
To solve this part I used `itertools.combinations`. this functions allows us to generate r length subsequences of elements from the input iterable. This means we can pass in the `numbers` and set the `r` parameter to `2` and get all the combinations with two elements.
```python
combinations = itertools.combinations(numbers, 2)
```

The next part is to simply iterate through these combinations and look for the combinations where the sum is equal to `2020` and return the product.
```python
part1_ans = [reduce(mul, c) for c in combinations if sum(c) == 2020]
```
Even though this would create a list with all the combinations where the sum is `2020` the length of the list should only be `1` element if the input data is correct.

### Part 2
For part 2 of this day we only have to change one single character. Instead of combinations of length `2` we want combinations with length `3`. This is simply done by changing the `r` argument of `combinations` 
```python
combinations = itertools.combinations(numbers, 3)
```


---



## --- Day 2: Password Philosophy ---
[Solution!](./02/solution.py)

### Input 
The second day input is a bit more complicated than the first one. The input for day `2` consist of mutiple lines, where each line contains a integer range, a character, and a string.
F.eks.

```
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```

The first this I did was to read the entire input as a string.
```python
s = open("input.txt").read()
```

After this I used a simple regex to modify each line in the input.
```python
s = re.sub(r"-|:", " ", read_string("input.txt"))
# 1-3 a: abcde -> 1 3 a abcde
```
This is done to make it easier to split each line and extract the information. Now I can simply use `split()` to end up with something like:
```
["1", "3", "a", "abcde"]
```

### Part 1
The sultion for this task is very simple. After the input parsing I have an array of arrays, where each sub-array is on the format: `[start, end, character, string]`.

- Step 1: Iterate through the lines
`for s,e,c,s in all_lines:`
- Step 2: Get the count for `letter` in the string
`if s.count(c): result += 1`
- Step 3: Check if count is in the range `start-end`, if yes update result

This can all be done in a single list comprehension:
```python
return sum([s.count(c) in range(int(s), int(e)+1) for s,e,c,s in all_lines])
```

### Part 2
In part 2 we are suppose to check if the character `c` appears on either index `s` or index `e` in the string `s`. The password is valid if the chracter appears on at least, and only one of the indexes. In other words this can be expressed as a `XOR` opperation.

| s | e | valid |
|:-:|:-:|:-----:|
| 0 | 0 |   0   |
| 1 | 0 |   1   |
| 0 | 1 |   1   |
| 1 | 1 |   0   |


```python
return sum([(p[int(s)-1]==c) ^ (p[int(e)-1]==c) for s,e,c,s in all_lines])
```


---



## --- Day 3: Toboggan Trajectory ---
[Solution!](./03/solution.py)

### Input
The input for this task consist of mutiple lines of strings. Each character in a line is either a `#` or a  `.`. All the lines together make up a grid, where `#` represents a tree and `.` represents an empty space. See example under.

```
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
```

I chose a 2D array representation of the grid. To acheive this, i simply read every line, and split each of the strings into char arrays.

```python
[[c for c in s.strip()] for s in open("input.txt")]
```

### Part 1
In this part we are suppose to get the number of trees we hit if we travel through the grid in a certain direction. In this case the direction is `delta x = 3, delta y = 1`. The starting position is `x = 0, y = 0`. This means for every iteration the new position is: `current_pos + deltas`

The code:
```python
H, W = len(grid), len(grid[0])
dx = 3
dy = 1
return sum(grid[i * dy][(i * dx) % W] == "#" for i in range(H // dy))
```

Lets break down the code.
- `i * delta` will get the position on `x` and `y` after i steps
- `% W` in the x-axis is to ensure we loop around to the start when out of bounds
- `range(H // dy)` will loop the number of steps to reach the bottom `y`


### Part 2
For part 2 this day we should simply do the same, but for multiple paths down the grid. We should then multiply the results from each of the paths

We simply add another loop, looping over the different paths, and use `reduce` to multiply the results together.

```python
H, W = len(grid), len(grid[0])
dirs = [(1,1),(3,1),(5,1),(7,1),(1,2)]
return reduce(mul, [sum(grid[i * dy][(i * dx) % W] == "#" for i in range(H // dy)) for dx, dy in dirs])
```



---



## --- Day 4: Passport Processing ---
[Solution!](./04/solution.py)

### Input
The input for this day is a lot of passports and their information. Each passport is separated by a line with an empty newline(`\n`). For each passport there are a lot of fields with information. A field is represented as: `key:value` in the string.

Example input:
```
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
```

As we can see fields within the same passport can be on different lines as well. To make it a bit easier I simplified the input using some regex in the beginning.
```python
text = open("input.txt").read()
text = re.sub(r"(.)\n", r"\1 ", text)
```
After this regex substitution the input looks like this: 

```
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm
iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929
hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm
hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in
```

Each of the lines now represents a full passport.
The next step was to iterate through the lines and store all the passports. For each passport I created a dictionary with all its entries, and appended this to a list.
```python
lines = [[tuple(s.split(":")) for s in l.split()] for l in text.split("\n")]
passwords = [{k: v for k, v in l} for l in lines]
```

After this the `passsports` variable is a list with dictionaries.

### Part 1
After creating the solid datastructure this part was really easy. All i had to do here was to iterate through the passports, and check the length of each dict. There are 2 cases where a passport is valid; all fields are there, or `cid` is missing. This simple check takes care of that.

```python
def is_valid_1(p):
    return len(p) == 8 or len(p.keys()) == 7 and "cid" not in p.keys()
```

After defining this function we can simply do:
```python
sum(is_valid_1(p) for p in passports)
```


### Part 2
In this part the criteria for a valid passport is more strict. In addition to the requirements from part 1 there are some extra ones for each field. here is a list of requirements:

- `byr` (Birth Year) - four digits; at least `1920` and at most `2002`.
- `iyr` (Issue Year) - four digits; at least `2010` and at most `2020`.
- `eyr` (Expiration Year) - four digits; at least `2020` and at most `2030`.
- `hgt` (Height) - a number followed by either `cm` or `in`:
    - If `cm`, the number must be at least `150` and at most `193`.
    - If `in`, the number must be at least `59` and at most `76`.
    `hcl` (Hair Color) - a # followed by exactly six characters `0-9 or a-f`.
- `ecl` (Eye Color) - exactly one of: `amb` `blu` `brn` `gry` `grn` `hzl` `oth`.
- `pid` (Passport ID) - a nine-digit number, including leading zeroes.
- `cid` (Country ID) - ignored, missing or not.

There are basically 3 different categories of check that are suitable in my opinion.
1. A range - `byr`, `iyr` and `eyr` 
2. String mathing - `hgt`, `pid` and `hcl`
3. Sub-set `ecl`

- The range matching is done using regex on the form:
```python
min_range <= passport[key] <= max_range
```
- The string matching is done using regex
```python
re.match(regex, passport[key])
```
- The sub-set matching is done simply with
```python
passport[key] in some_defined_values
```

Each regex I used for `hgt`, `pid` and `hcl` is listed under:
- `hgt` : `(^(1[5-8]\d|19[0-3])cm$|^(([5-6]\d|7[0-6])in)$)`
- `pid` : `^\d{9}$`
- `hcl` : `^#[\d|a-f]{6}$`

To sum up. For each of the passports I test these requirements, in addtion to the requirement from part 1, and if there are all met the passport is valid, and we increase the sum.

---



## --- Day 5: Passport Processing ---
[Solution!](./05/solution.py)

### Input
The input for this day required no parsing at all. I simply read the input file and store each line in a array. This is done with this code:

```python
seats = [f(l.strip()) for l in open(filename)]
``` 

Example input looks like this.
```
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
```

### Part 1
First thing we need to do is to extract the seat ID from a string. We start looking at the row.
We know that `F` means select the lower half of the interval, and `B` means select the higher half of the interval. I quickly discovered that we can directly map the `F` and the `B` characters in the string to the bits in a byte. This means a `B` at position `0` in the string would result in setting bit 7 in a byte to 1. I applied this strategy and it worked perfectly.

A row number can then be extracted with the following code:

```python
row = sum([int(c=="B") << 6-i for i, c in enumerate(s[:7])])
```

The process for the columns are exactly the same, except we are only dealing with 3 bits, instad of 8.
```python
col = sum([int(c=="R") << 2-i for i, c in enumerate(s[7:])])
```

After this is extracted we can simply calculate the ID with `row * 8 + col`

We store this result in a list, and simply select the max of that list with
```python
result = max(all_IDs)
```

### Part 2
Part 2 was pretty straight forward at this point. We have all the id's stored in a list, and we know that there is a gap in that list that is supposed to be our ID. This means if the id's are `[3,4,5,7,8,9]`, we know that our id is 6.

```python
for i, ID in enumerate(all_IDs[:-1]):
    if res[i] != res[i+1] - 1:
        return ID + 1
```

**See how the plane fills up**
![alt](05/animations/viz.gif)



---



## --- Day 6: Custom Customs ---
[Solution!](./06/solution.py)

### Input
The input for this day is contains lines where each line is either a new-line of a string. The input consist of groups of people answering questions, and each group is separated by an empty newline.

Example input:
```
abc

a
b
c

ab
ac

a
a
a
a

b
```

The first thing I did was to split all the grups. This is done with:
```python
groups = re.split(r"\n\n", text)
```

Inside every group there are people answering questions and these are seperated with a single newline. I therefor split each group into a list with the answers for every person. This is done with: 

```python
l = group.split("\n")
```

First I get the number of people with:

```python
people = len(l)
```

For each of the people we need to count their answers. This is done using `collections.Counter`. We then add the counts for each person to a global list together with the number of people in that group. This is done with a tuple.
```python
c = Counter(c for ans in l for c in ans)
ret.append((c, reps))
```

### Part 1
After processing the input data, this task is really simple to solve. We just need to iterate through the list of groups and get the number of questions that someone answered yes to. This is done with:
```python
sum(len(c.keys()) for c,reps in counts)
```

### Part 2
Part 2 asks for the number of questions where all people in a group answered yes. After creating the datastructures this can easially be extracted with:
```python
sum(sum(v == people for v in c.values()) for c,people in counts)
```

---

## --- Day 7: Handy Haversacks ---
[Solution!](./07/solution.py)

### Input
This day was the hardest one so far. A big reason for this was because of all the input parsing needed. The input is given as lines with strings. Each line describes what bags a certain bag can contain.

Example input:
```
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
```

This Input get be represented as a graph. And a good idea is to build that graph. I chose a dictionary representation of the graph.

The first step to doing this is to modify the input lines a little bit using a regex. I replaced all `bags` with just `bag` to avoid getting any key errors. As well as this, I removed some spacing, and puntiation. This is done with:
```python
data = open("input.txt").read()
subs = {", ": ",", "\.": "", "bags": "bag", r"(\d)\s": r"\1:"}
for k, v in subs.items():
    data = re.sub(k, v, data)
```

After this is done, I split the line into `key, values` pairs:
```python
data = [line.split(" contain ") for line in data.split("\n")][:-1]
```

When this is done we can start extracting the values. This is done by splitting the values on `,` and looping over them. For every iteration we use the bag name as a key, and the number as value in a sub dictionary. When all the values are extracted we add the sub dict to the main dict.
```python
v_list = values.split(",")
sub_dict = {}
for v in v_list:
    num, tag = v.split(":")
    sub_dict[tag] = int(num)
D[key] = sub_dict
```

### Part 1
After creating the representation of the graph this part was a pretty straight forward DFS/BFS. We simply start by initiating a queue with all the keys. For each iteration we pop the first element in the queue. If the target is in the elemts children we add 1 to the score. Otherwise we add all the children to the q.

```python
while q:
    k, start_node = q.popleft()
    if start_node in SEEN:
        continue
    if TARGET in D[k].keys():
        total += 1 
        SEEN.add(start_node)
    for child in D[k]:
        q.appendleft((child, start_node))
```

### Part 2
This part is similar to part 1. Instead of starting with all the keys, we only initiate the que with `shiny gold bag` as key. The we search down throught the children. For every children we update a multiplier depending on how many bags a bag can contain.

```python
while q:
    k, multiplier = q.popleft()
    # Get the children and their values of current bag
    for child_key, child_value in D[k].items():
        new_mul = multiplier * child_value
        total += new_mul
        q.appendleft((child_key, new_mul))
```


---



## --- Day 8: Handheld Halting ---
[solution!](./08/solution.py)


### Input
The input for this day contains multiple lines, where on each line there is a instruction. The instruction contains a operation, and a value. F.eks.
```
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
```

I simply read each line and stored the operation, and value as a sub-list inside a list. This is done with: 
```python
data = []
with open(filename) as f:
    for line in f:
        op_code, val = line.split()
        data.append([op_code, int(val)])
```
The results from this is a list that looks something like this: `[["nop", 0], ["acc", 1], ["jmp", 4]....]`


### Part 1
I chose to go for a class implementation this day. This is mainly because it looks like a kind of problem that can be built on top on the next days 

The first thing I did was to create a function to handle each of the operations.
```python
    def op_acc(self, v):
        self.acc += v

    def op_jmp(self, v):
        self.index += v - 1 # -1 due to index increare in main loop

    def op_nop(self, v):
        pass
```

I also created a dict which map the `op code` strings to each function.
```python
op_funcs = {
    "acc": self.op_acc,
    "jmp": self.op_jmp,
    "nop": self.op_nop
}
```

After this is done we can simply perform the correct action with `op_funcs[current_op_code](current_value)`

The next part was to actually write the code to execute the instrctions from the input. I wrote a function for this as well, called `execute_op_codes`. The main parts of this function looks like this: 
```python
while True:
    op_code, val = self.input[self.index]
    self.op_funcs[op_code](val)
    self.index += 1
```
We simply extract the current instruction and make a call to the correct function.

For now this is a infinite loop that will never end (before a `IndexError` of course). For part 1 we should exit the loop when a instruction is executed for the second time. To achieve this we simply use a set which we add every instruction to. If a new instruction is already in the set, we exit.
```python
if self.index in seen:
    break
SEEN.add(self.index)
```
After this the results are be stored in the instance variable `self.acc`

### Part 2
For this part we want the program to reach the bottom of the instructions, and terminate normaly. The first thing I did was to add another check into the `while True` loop from part 1:

```python
if self.index >= self.num_op_codes - 1:
    self.normal_term = true
    break
if self.index in seen:
    self.normal_term = false
    break
```

Now that this is in place we need to actully implement the switching of the operations. The first thing I did was to create a `dict` contains the possible swaps: 
```python
swaps = {"nop": "jmp", "jmp": "nop"}
```
Even though its only 2 possible swaps here, it could be more. The next part was to find all the indexes of the current items:
```python
for key, value in swaps.items():
    replacements = [i for i, val in enumerate(self.input) if val[0] == key]
```

Now we can loop over the replacement indexes, and replace one at a time.
```python
for r in replacements:
    self.input[r][0] = value
    self.execute_op_codes()
    if self.normal_term:
        return self.acc

    # Swith back if it didn't work out
    self.input[r][0] = key
```
the last line of code make sure that only a single operation is switches at a time. For every iteration we simply run the `execute_op_codes` function, and check whether the termination was normal.


---


## --- Day 9: Encoding Error ---
[Solution!](./09/solution.py)

### Input 
The input for this day consist of numbers seperated by a newline(`\n`). 
For example:
```
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
```

To read the input I used a very simple list comprehension to store the numbers in a list:
```python
data = [int(l.strip()) for l in open("input.txt")]
```

### Part 1
To solve this part I created a loop to loop through all the numbers in the list. We can skip the first `25` numbers, because no check is need for these.
```python
step = 25
for i in range(step, len(data)):
```

The next part is to extract the `25` numbers before the current number. This is done with array slicing.
```python
nums = data[i-step:i]
```
Now all that remains is to check whether `2` of the numbers in that list produce a sum that is equal to the current number. To achieve this I used `itertools.combinations`. This part of the task is exactly the same as day 1. `itertools.combinations` with `r` argument set to `2` will produce all possible combinations of length `2` from the numbers in `nums`. All that is left to do then is to check if the sum of any combination is equal to the target. If not we have the result.
```python
if not any((x + y == target) for x, y in itertools.combinations(nums, 2)):
    return target
```

### Part 2
Part 2 for this day is to find a contiguous set of numbers inside the array that adds up to the results from part 1.

I solved this with 2 nested for-loops. The first for loop defines the start of the range, and the second defines the end of the range. For every new `j` we simply check if the sum of that range is equal to the target. If it is, we return the answer, if it is smaller we continue expanding the range, if it is bigger than the target we move the start index of the range up.
```python
for i in range(len(data)):
    for j in range(i+1, len(data)):
        current_range = data[i:j+1]
        current_sum = sum(current_range)
        # Return results if current sum match target
        if current_sum == target:
            return min(current_range) + max(current_range)

        # if current sum is already over target, no need to continue
        if current_sum > target:
            break
```



---


## --- Day 10: Adapter Array ---
[Solution!](./10/solution.py)

### Input 
This days input was a file with integers separated by newlines(`\n`). I simply read all the integers into a array with a list comprehension.

```python
data = [int(l.strip()) for l in open("input.txt")]
```

I then added `0` and the max built in adapter value to the array.
```python
data.append(0)
data.append(max(data) + 3)
```
After this I sorted the array:

```python
sort = sorted(data)
```
After these steps the input array is ready.

### Part 1
The first thing I did for this part was to create a dictionary to store all the different differences of jolts.
```python
diffs = defaultdict(int)
```
The next step was to loop over the sorted array. For each step we find the potential next adapters. These are the steps inside the loop.
1. Find the next potential adapters from the sorted array
2. Select the minimum of the potential adapters
3. Update the diffrences dict

```python
for i, current_adapter in enumerate(sort[:-1]):
    next_adapters = [n for n in sort[i+1:i+4] if n - current_adapter <= 3]
    diffs[min(next_adapters) - current_adapter] += 1
return diffs[1] * diffs[3]
```
Note that since we assume all the values in the array are distinct we only need to search 3 places ahead in the array. Any index over that would generate a difference larger than 3, which breaks the rules.

The last step for this part is to simply return the product of `diffs[1]` and `diffs[3]`

### Part 2
This part was maybe the hardest one yet. I tried brute forcing it, but realized soon that it would take way to long (I even fried my computer at a point, and had to reboot...). I then started on a more dynamic programming aproach, which worked out nicely.

I created a recursive function that takes the current index as argument. The structure is actually very similar to the one in part 1, except we also explore the other potentail adapters(not just the minimum). It consist of the following steps:

1. If index == len(data) -1: return 1
2. If index has been visited before return previously found value
3. Loop over potential next adapters, and call function recursivly
3. Update value for current index

Here is the function: 
```python
FOUND = {}
def rec(i):
    current = sort[i]
    if i >= len(sort) -1:
        return 1
    # If path has been explored from this point and out
    if i in FOUND.keys():
        return FOUND[i]

    # call function recursively and sum up the total and add to dict
    tot = sum(rec(j+i+1) for j, x in enumerate(sort[i+1:i+4]) if x - current <= 3)
    FOUND[i] = tot

    return tot
```

The beauty about this implementation is that when it has explored the path from a current index, it doesn't have to do it again, instead simply do a lookup in a dictionary. If we take a look at the first example input; the execution would be like this:
```
Enter:  0
Enter:  1
Enter:  4
Enter:  5
Enter:  6
Enter:  7
Enter:  10
Enter:  11
Enter:  12
Enter:  15
Enter:  16
Enter:  19
Enter:  22
BACKTRACK:  19
BACKTRACK:  16
BACKTRACK:  15
BACKTRACK:  12
BACKTRACK:  11
Enter:  12
FETCHING FROM DICT
BACKTRACK:  10
BACKTRACK:  7
BACKTRACK:  6
Enter:  7
FETCHING FROM DICT
BACKTRACK:  5
Enter:  6
FETCHING FROM DICT
Enter:  7
FETCHING FROM DICT
BACKTRACK:  4
BACKTRACK:  1
BACKTRACK:  0

```
When the recursive function reaches a number it has seen before it doesn't continue deeper, but simply looks up the prevous value for that number. The total number of calls to the recursive function in this case is `17`. If we however remove the lookup test, its `58`. The results are still the same, it just takes forever when the input is large enough.


---


## --- Day 11: \<TITLE\> ---
[Solution!](./11/solution.py)

### Input 
This day's input consist of multiple lines, where each line contains chracters that are one of: `#`, `L` or `.`. All the lines make up a grid.

For example:
```
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
```

I read all the lines and characters into a 2D array (a matrix/grid). This was done using a list comprehension:
```python
[[c for c in s.strip()] for s in open("input.txt")]
```

After this for I mapped the different characters to integers in the grid. This is done for animation purposes later. From now on keep in mind this mapping:
```python
{"#": -1, "L": 1, ".": 0}
```


### Part 1
I quickly realized this task was very similar to the popular **game of life**. The rules were only a bit different. In addition to this we deal with empty spaces (`.`). My first step to solving this task was to manage to do one single iteration on the grid. A iterations contains these simple steps:
1. Loop over every element in the grid
2. Find all neighbors
3. Count number of occupied seats among neighbors
4. Change current element based on count

Another thing to keep in mind is that we have to make a copy of the current board, and make changes to the copy during the iteration. This is because we don't want previous updates within the same iteration to affect the next updates.

#### Looping over the grid
```python
for y, row in enumerate(grid):
    for x, elem in enumerate(row):
        # Calculate new state of element
```

#### Find the neighbors and count them
The first thing I did here was to define all the possible directions we can move from the current cell.
```python
dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
```
The next thing is to loop over all these and count the occupied ones:
```python
tot = 0
for dx, dy in dirs:
    new_x = x + dx
    new_y = y + dy

    # Test if array indexes are out of bounds
    if not 0 <= new_x < W or not 0 <= new_y < H:
        continue
    new_val = grid[new_y, new_x]
    if new_val == -1:   # -1 is #
        tot += 1
```

#### Update current element
After the previous step we have the number of occupied neighbors, and can now update according to the rules (remember the mapping from characters to ints I made):
```python
# Set the new values with regards to the rules of seatchanging
if grid[y, x] == 1 and tot == 0:
    new_grid[y, x] = -1

elif grid[y, x] == -1 and tot >= num_occ:
    new_grid[y, x] = 1
```

This concludes a iteration. The next step was to then integrate the support for multiple iterations. I simply wrapped all the previous code inside a `while True` and added a check thats checks if no change during the iteration happend:

```python
while True:
    new_grid = grid.copy()

    # Perform single iteration here

    if np.array_equal(grid, new_grid):
        return np.count_nonzero(grid == -1), arrays
    grid = new_grid
```

After all these steps I got the correct result, and also generated an animation showing how the seating arrangments changes (check [folder](./11/animations/part1.gif) for better quality):

![Part 1 anim](./11/animations/part1.gif)

### Part 2
It was not too difficult to extend my implementation from part 1 to do this part. In the previous part we only checked the next neighbors, but in this part we will do some sort of *ray tracing* in a direction until we hit something. The main parts i changed look like this:

```python
for dx, dy in dirs:
    for dist in range(1, max_dist+1):
        new_x = x + dx*dist
        new_y = y + dy*dist

        # Test if array indexes are out of bounds
        if not 0 <= new_x < W or not 0 <= new_y < H:
            break
        new_val = grid[new_y, new_x]
        if new_val == -1:
            tot += 1
        if new_val != 0:
            break
```

As you can see we added a new loop that increases the distances in a certain direction until it hits something (or is outside the grid). The calculation of the new `x` and `y` coordinates have now changed a little bit:

```python
new_x = x + dx
new_y = y + dy

#     |
#     V 

new_x = x + dx*dist
new_y = y + dy*dist
```

As well as minor changes to the if tests, and updating the number of required occupied seats for change state. After tall these small tweaks to part 1, I got the correct result. Animation for this part as well of course: 

![Part 2 anim](./11/animations/part2.gif)



---


## --- Day 12: \<TITLE\> ---
[Solution!](./12/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 13: \<TITLE\> ---
[Solution!](./13/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 14: \<TITLE\> ---
[Solution!](./14/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 15: \<TITLE\> ---
[Solution!](./15/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 16: \<TITLE\> ---
[Solution!](./16/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 17: \<TITLE\> ---
[Solution!](./17/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 18: \<TITLE\> ---
[Solution!](./18/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 19: \<TITLE\> ---
[Solution!](./19/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 20: \<TITLE\> ---
[Solution!](./20/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 21: \<TITLE\> ---
[Solution!](./21/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 22: \<TITLE\> ---
[Solution!](./22/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 23: \<TITLE\> ---
[Solution!](./23/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 24: \<TITLE\> ---
[Solution!](./24/solution.py)
### Input 

### Part 1

### Part 2


---


## --- Day 25: \<TITLE\> ---
[Solution!](./25/solution.py)
### Input 

### Part 1

### Part 2


---


