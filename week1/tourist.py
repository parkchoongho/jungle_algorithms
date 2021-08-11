import sys
from itertools import permutations

num_count = int(sys.stdin.readline())

permu_list = [None] * num_count
for i in range(num_count):
    permu_list[i] = i

final_permu_list = list(permutations(permu_list))

road_info = [None] * num_count
for i in range(num_count):
    input_list = list(map(int, sys.stdin.readline().split()))
    road_info[i] = input_list


min = sys.maxsize
for permu in final_permu_list:
    cost = 0
    foo = list(permu)
    foo.append(foo[0])
    is_no_road = False
    for i in range(len(foo) - 1):
        if road_info[foo[i]][foo[i + 1]] == 0:
            is_no_road = True
            break
        cost += road_info[foo[i]][foo[i + 1]]
    if is_no_road:
        continue
    if min > cost:
        min = cost

print(min)
