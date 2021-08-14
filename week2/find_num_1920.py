import sys


def find_half(input_list, value):
    start = 0
    end = len(input_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if input_list[mid] > value:
            end = mid - 1
        elif input_list[mid] < value:
            start = mid + 1
        else:
            return 1
    return 0


total_count = int(sys.stdin.readline())

total_list = list(map(int, sys.stdin.readline().split()))

total_list.sort()


input_count = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))

for input in input_list:
    print(find_half(total_list, input))
