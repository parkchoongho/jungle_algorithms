import sys
test_num = int(sys.stdin.readline())

word_list = []

for _ in range(test_num):
    word = sys.stdin.readline().rstrip()
    if word in word_list:
        continue
    word_list.append(word)


def merge_sort(input_list):
    total_length = len(input_list)
    if total_length == 1:
        return input_list
    forward_list = input_list[0: total_length // 2]
    backward_list = input_list[total_length // 2: total_length]

    forward_list = merge_sort(forward_list)
    backward_list = merge_sort(backward_list)

    forward_index = 0
    backward_index = 0
    total_list = [None] * total_length
    total_list_index = 0
    while forward_index < len(forward_list) and backward_index < len(backward_list):
        if len(forward_list[forward_index]) > len(backward_list[backward_index]):
            total_list[total_list_index] = backward_list[backward_index]
            backward_index += 1
        elif len(forward_list[forward_index]) == len(backward_list[backward_index]):
            for i in range(len(forward_list[forward_index])):
                if forward_list[forward_index][i] > backward_list[backward_index][i]:
                    total_list[total_list_index] = backward_list[backward_index]
                    backward_index += 1
                    break
                elif forward_list[forward_index][i] < backward_list[backward_index][i]:
                    total_list[total_list_index] = forward_list[forward_index]
                    forward_index += 1
                    break
        else:
            total_list[total_list_index] = forward_list[forward_index]
            forward_index += 1
        total_list_index += 1

    while forward_index < len(forward_list) and total_list_index < total_length:
        total_list[total_list_index] = forward_list[forward_index]
        forward_index += 1
        total_list_index += 1
    while backward_index < len(backward_list) and total_list_index < total_length:
        total_list[total_list_index] = backward_list[backward_index]
        backward_index += 1
        total_list_index += 1
    return total_list


sorted_list = merge_sort(word_list)


for word in sorted_list:
    print(word)
