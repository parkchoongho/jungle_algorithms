num = int(input())

input_list = []

for _ in range(num):
    input_list.append(int(input()))


def merge_sort(input_list):
    if len(input_list) == 1:
        return input_list
    forward_list = input_list[0 : len(input_list) // 2]
    backward_list = input_list[len(input_list) // 2 : len(input_list)]

    forward_list = merge_sort(forward_list)
    backward_list = merge_sort(backward_list)

    forward_index = 0
    backward_index = 0
    total_list = []
    while forward_index < len(forward_list) and backward_index < len(backward_list):
        if forward_list[forward_index] > backward_list[backward_index]:
            total_list.append(backward_list[backward_index])
            backward_index += 1
        else:
            total_list.append(forward_list[forward_index])
            forward_index += 1
    while forward_index < len(forward_list):
        total_list.append(forward_list[forward_index])
        forward_index += 1
    while backward_index < len(backward_list):
        total_list.append(backward_list[backward_index])
        backward_index += 1
    return total_list


print(merge_sort(input_list))
