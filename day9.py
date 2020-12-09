from itertools import islice, combinations
from collections import deque

test_input = """\
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
576\
""".split("\n")

def parse_numbers(lines):
    return (int(line.strip()) for line in lines)


def is_sum_of_two(number, numbers):
    return any(a+b==number for a, b in combinations(numbers, 2))

def solution_1(lines, N=25):
    numbers = parse_numbers(lines)
    number_buffer = deque(islice(numbers, N), N)
    while True:
        new_number = next(numbers)
        if not is_sum_of_two(new_number, number_buffer):
            return new_number
        number_buffer.append(new_number)

def solution_2(lines, wanted_sum):
    numbers = parse_numbers(lines)
    cur_buffer = deque(islice(numbers, 2))
    cur_sum = sum(cur_buffer)
    while cur_sum != wanted_sum:
        if cur_sum > wanted_sum:
            cur_sum -= cur_buffer.popleft()
        else:
            number = next(numbers)
            cur_sum += number
            cur_buffer.append(number)
    return min(cur_buffer) + max(cur_buffer)

assert solution_1(test_input, 5) == 127
print(solution_1(open("input/day9.txt")))
print(solution_2(open("input/day9.txt"), 375054920))
      
