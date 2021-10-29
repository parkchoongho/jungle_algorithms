import sys


def merge_sort(int_list: list):
    if len(int_list) == 1:
        return int_list
    forward_list = int_list[:len(int_list) // 2]
    backward_list = int_list[len(int_list) // 2:]

    sorted_forward_list = merge_sort(forward_list)
    sorted_backward_list = merge_sort(backward_list)

    final_list = []

    i = 0
    j = 0

    forward_length = len(sorted_forward_list)
    backward_length = len(sorted_backward_list)

    while i < forward_length and j < backward_length:
        if sorted_forward_list[i] > sorted_backward_list[j]:
            final_list.append(sorted_forward_list[i])
            i += 1
        else:
            final_list.append(sorted_backward_list[j])
            j += 1

    if i != forward_length:
        while i < forward_length:
            final_list.append(sorted_forward_list[i])
            i += 1

    if j != backward_length:
        while j < backward_length:
            final_list.append(sorted_backward_list[j])
            j += 1

    return final_list


input_str = sys.stdin.readline().rstrip()

int_list = []

for c in input_str:
    int_list.append(int(c))

answer_list = merge_sort(int_list)

answer = ''

for ans in answer_list:
    answer += str(ans)

print(answer)
