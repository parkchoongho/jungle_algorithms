from typing import MutableSequence


def heap_sort(input_list: MutableSequence) -> None:
    def down_heap(input_list, left: int, right: int):
        temp = input_list[left]

        parent = left

        while parent < (right + 1) // 2:
            left_child = 2 * parent + 1
            right_child = left_child + 1
            child = right_child if (right_child <= right and input_list[right_child] > input_list[left_child]) else left_child
            if temp >= input_list[child]:
                break
            input_list[parent] = input_list[child]
            parent = child
        input_list[parent] = temp

    size = len(input_list)

    for i in range((size - 1) // 2, -1, -1):
        down_heap(input_list, i, size - 1)

    for i in range(size - 1, 0, -1):
        input_list[0], input_list[i] = input_list[i], input_list[0]
        down_heap(input_list, 0, i - 1)


if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    input_list = [None] * num

    for i in range(num):
        input_list[i] = int(input(f'input_list[{i}]: '))

    heap_sort(input_list)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'input_list[{i}] = {input_list[i]}')
