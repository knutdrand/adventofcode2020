from more_itertools import split_at

test_input = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in\
""".split("\n")

invalid_passport_input = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007\
""".split("\n")

valid_passport_input = """\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719\
""".split("\n")

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

def _validate_height(text):
    if not text[:-2].isdigit():
        return False
    m, n = (text[-2:], int(text[:-2]))
    return (m=="cm" and 150<=n<= 193) or (m=="in" and 59<=n<=76)

validation={"byr": lambda x: 1920 <= int(x) <= 2002,
            "iyr": lambda x: 2010 <= int(x) <= 2020,
            "eyr": lambda x: 2020 <= int(x) <= 2030,
            "hgt": _validate_height,
            "hcl": lambda x: len(x) == 7 and x.startswith("#") and all(c in "abcdef0123456789" for c in x[1:]),
            "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
            "pid": lambda x: len(x)==9 and x.isdigit()}


def get_passport(line):
    return dict(p.split(":") for p in line.split())

def get_passports(lines):
    chunks = split_at(lines, lambda line: not line.strip())
    chunks = (" ".join(chunk) for chunk in chunks)
    return (get_passport(chunk) for chunk in chunks)

def has_valid_fields(passport):
    return not (required_fields-set(passport.keys()))

def is_valid(passport):
    return all(key in passport and validation[key](passport[key])
               for key in validation)

def solution_1(lines):
    return sum(has_valid_fields(passport) for passport in
               get_passports(lines))

def solution_2(lines):
    return sum(is_valid(passport) for passport in get_passports(lines))

assert solution_1(test_input) == 2
print(solution_1(open("input/day4.txt")))

assert solution_2(invalid_passport_input) == 0
assert solution_2(valid_passport_input) == 4, solution_2(valid_passport_input)
print(solution_2(open("input/day4.txt")))
