import re

test_input = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc\
""".split("\n")

def get_matches(lines):
    return (re.match("(\d+)-(\d+) (.): (\w+)", line).groups() for line in lines)

def solution_1(lines):
    matches = get_matches(lines)
    are_valid = (int(low) <= password.count(char) <= int(high)
                 for low, high, char, password in matches)
    return sum(are_valid)

def solution_2(lines):
    matches = get_matches(lines)
    are_valid = ((password[int(low)-1]==char) ^ (password[int(high)-1]==char)
                 for low, high, char, password in matches)
    return sum(are_valid)

assert solution_1(test_input) == 2
assert solution_2(test_input) == 1
print(solution_1(open("input/day2.txt")))
print(solution_2(open("input/day2.txt")))
