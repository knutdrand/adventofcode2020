from itertools import combinations
from math import prod

test_input = """\
1721
979
366
299
675
1456\
""".split("\n")

def find_sum_equal(numbers, total, n=2):
    return next(t for t in combinations(numbers, n)
                if sum(t) == total)

def solution_1(lines):
    numbers = [int(n) for n in lines]
    return prod(find_sum_equal(numbers, 2020))

def solution_2(lines):
    numbers = [int(n) for n in lines]
    return prod(find_sum_equal(numbers, 2020, 3))


assert solution_1(test_set) == 514579
assert solution_2(test_set) == 241861950
    
print(solution_1(open("input/day1.txt")))
print(solution_2(open("input/day1.txt")))


