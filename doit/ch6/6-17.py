from typing import MutableSequence


def fsort(input_list: MutableSequence, max: int) -> None:
    length = len(input_list)

    accumulate_list = [0] * (max + 1)
    operation_list = [0] * length

    for i in range(length):
        accumulate_list[input_list[i]] += 1

    for i in range(1, max + 1):
        accumulate_list[i] += accumulate_list[i - 1]

    for i in range(length - 1, -1, -1):
        accumulate_list[input_list[i]] -= 1
        operation_list[accumulate_list[input_list[i]]] = input_list[i]

    for i in range(length):
        input_list[i] = operation_list[i]


def counting_sort(input_list: MutableSequence) -> None:
    fsort(input_list, max(input_list))


if __name__ == '__main__':
    print('도수 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    input_list = [None] * num

    for i in range(num):
        while True:
            input_list[i] = int(input(f'input_list[{i}]: '))
            if input_list[i] >= 0:
                break

    counting_sort(input_list)

    print('오름차순으로 정렬했습니다.')

    for i in range(num):
        print(f'input_list[{i}] = {input_list[i]}')
