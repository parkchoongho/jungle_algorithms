import sys

a_cnt, b_cnt = map(int, sys.stdin.readline().split())

a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))

a_list.sort()
b_list.sort()

i = 0
j = 0

same_num_cnt = 0

len_a = len(a_list)
len_b = len(b_list)

while i < len_a and j < len_b:
    if a_list[i] > b_list[j]:
        j += 1
    elif a_list[i] < b_list[j]:
        i += 1
    else:
        same_num_cnt += 1
        i += 1
        j += 1

print(a_cnt + b_cnt - same_num_cnt * 2)
