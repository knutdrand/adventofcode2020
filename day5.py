from more_itertools import pairwise

def get_seatid(boarding_pass):
    lookup = {"B": 1, "F": 0, "R": 1, "L": 0}
    binary_rep = "".join(str(lookup[c]) for c in boarding_pass)
    return int(binary_rep, 2)

assert get_seatid("BFFFBBFRRR") == 567
assert get_seatid("FFFBBBFRRR") == 119
assert get_seatid("BBFFBBFRLL") == 820

def solution_1(lines):
    return max(get_seatid(line.strip()) for line in lines)

def solution_2(lines):
    seat_ids = sorted(get_seatid(line.strip()) for line in lines)
    return next(a+1 for a, b in pairwise(seat_ids) if b != a+1)


print(solution_1(open("input/day5.txt")))
print(solution_2(open("input/day5.txt")))
