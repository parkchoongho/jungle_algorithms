def counting_sort(input_list, max):
    length = len(input_list)
    accumulate_list = [0] * (max + 1)
    sort_list = [0] * length

    for i in range(length):
        accumulate_list[input_list[i]] += 1

    for i in range(1, max):
        f[i]


num = int(input())

input_list = [0] * num
for i in range(num):
    input_list[i] = int(input())

counting_sort(input_list, max(input_list))
