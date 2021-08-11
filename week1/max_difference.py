import sys
from itertools import permutations

num_count = int(sys.stdin.readline())

input_list = list(map(int, sys.stdin.readline().split()))


permu_list = list(permutations(input_list))


max = 0
for i in permu_list:
    list_tuple = list(i)
    sum = 0
    for j in range(len(list_tuple) - 1):
        sum += abs(list_tuple[j] - list_tuple[j + 1])
    if sum > max:
        max = sum

print(max)
