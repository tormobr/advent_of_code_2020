# Advent of Code
This repo contains the solutions to the problems from [advent of code](https://adventofcode.com/2020)

---

### --- Day 1: Report Repair ---

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

#### Part 1
To solve this part I used `itertools.combinations`. this functions allows us to generate r length subsequences of elements from the input iterable. This means we can pass in the `numbers` and set the `r` parameter to `2` and get all the combinations with two elements.
```python
combinations = itertools.combinations(numbers, 2)
```

The next part is to simply iterate through these combinations and look for the combinations where the sum is equal to `2020` and return the product.
```python
part1_ans = [reduce(mul, c) for c in combinations if sum(c) == 2020]
```
Even though this would create a list with all the combinations where the sum is `2020` the length of the list should only be `1` element if the input data is correct.

#### Part 2
For part 2 of this day we only have to change one single character. Instead of combinations of length `2` we want combinations with length `3`. This is simply done by changing the `r` argument of `combinations` 
```python
combinations = itertools.combinations(numbers, 3)
```

---

### --- Day 2: Password Philosophy ---

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
```
1-3 a: abcde -> 1 3 a abcde
```
This is done to make it easier to split each line and extract the information. Now I can simply use `splitp()` to end up with something like:
```
["1", "3", "a", "abcde"]
```

#### Part 1
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

#### Part 2
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

### --- Day 3: Toboggan Trajectory ---

#### Part 1
- Find numbers of trees in path

#### Part 2
- Find number of trees in multiple paths

---

### --- Day 4: Passport Processing ---

#### Part 1
- Find number of passports that have all fields except for optional `cid`

#### Part 2
- Find number of passports the meets requirements from part 1 and in addition has requirements for each field in the passport

---

### --- Day 5: Passport Processing ---

#### Part 1
- Find the seat ID with the highest possible ID

#### Part 2
- Find "your" seat. The seat that is missing from the data. (not at the beginning or end)
![alt](05/animations/viz.gif)

---

### --- Day 6: Custom Customs ---

#### Part 1
- Find the number of questions anyone answered "yes" to in each group, and get sum of all groups

#### Part 2
- Get the number of questions everyone in the group answered yes to. And return sum of sums

---
