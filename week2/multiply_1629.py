import sys

num, quotinent, division = map(int, sys.stdin.readline().split())


def calculate_left(num: int, quotient: int, division: int):
    if quotient == 1:
        return num % division
    remain = calculate_left(num, quotient // 2, division)
    if quotient % 2 == 0:
        return remain * remain % division
    else:
        return remain * remain * num % division


print(calculate_left(num, quotinent, division))
