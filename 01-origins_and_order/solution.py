def answer(x, y, z):
    # validate for month
    def is_month(m):
        return m >= 1 and m <= 12

    # validate for day in a given month
    # no leap years
    def is_day(m, d):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return d >= 1 and d <= month_days[m-1]

    # check if the given list [month, day, year] makes a valid date
    # all numbers are in the range of 1-99 inclusive; so no need to
    # validate year
    def is_valid_date(p):
        m, d, y = p
        return is_month(m) and is_day(m, d)

    # return all six permutations of a triple
    def permutations(x, y, z):
        return [[x, y, z], [x, z, y], [y, x, z], [y, z, x], [z, x, y], [z, y, x]]

    # format given triple as MM/DD/YY (zero-filled)
    def format_date(p):
        m, d, y = p
        return '{0:02d}/{1:02d}/{2:02d}'.format(m, d, y)

    # check all permutations of the given triple for valid dates
    dates = list(set([format_date(p) for p in permutations(x, y, z) if is_valid_date(p)]))

    # we got our answer if there was only one valid date
    if len(dates) == 1:
        return dates[0]
    else:
        return "Ambiguous"

import random

def generate(n):
    def gen_number():
        if random.randint(0, 1) < 1:
            return random.randint(1, 99)
        else:
            return random.randint(1, 30)

    def gen_date():
        return [gen_number() for x in range(3)]

    return [gen_date() for x in range(n)]

def main():
    test_cases = [[19, 19, 3], [2, 30, 3]]
    test_cases.extend(generate(10))

    for case in test_cases:
        m, d, y = case
        print case, answer(m, d, y)

if __name__ == "__main__":
    main()
