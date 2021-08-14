import sys

N, M = map(int, sys.stdin.readline().split())

input_list = list(map(int, sys.stdin.readline().split()))


def find_cut_length(start, end, value):
    total_cut_length = 0
    while start <= end:
        mid = (start + end) // 2
        total_cut_length = calculate_legth(mid)
        if total_cut_length < value:
            end = mid - 1
        elif total_cut_length > value:
            start = mid + 1
        else:
            return mid
    if total_cut_length > value:
        return mid
    else:
        return mid - 1


def calculate_legth(cut):
    total_cut_legth = 0
    for input in input_list:
        if input > cut:
            total_cut_legth += (input - cut)
    return total_cut_legth


print(find_cut_length(1, max(input_list) - 1, M))
