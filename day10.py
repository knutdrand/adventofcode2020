from more_itertools import pairwise
from collections import Counter, deque

test_input = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3\
""".split("\n")

def parse_numbers(lines):
    return (int(line.strip()) for line in lines)

def solution_1(lines):
    joltages = sorted(parse_numbers(lines))
    diffs = (b-a for a, b in pairwise(joltages))
    counts = Counter(diffs)
    counts[min(joltages)] += 1
    return counts[1]*(counts[3]+1)

def solution_2(lines):
    joltages = [0] + sorted(parse_numbers(lines))
    counter = [0]*len(joltages)
    counter[0] = 1
    N = len(joltages)
    for i, jolt in enumerate(joltages):
        for j in range(i+1, min(i+4, N)):
            if joltages[j]-jolt<=3:
                counter[j] += counter[i]
    print(counter)
    return counter[-1]

assert solution_1(test_input) == 22*10
print(solution_1(open("input/day10.txt")))
assert solution_2(test_input) == 19208
print(solution_2(open("input/day10.txt")))
