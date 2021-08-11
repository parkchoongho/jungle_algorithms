from typing import MutableSequence


def quick_sort(input_list: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    pivot = input_list[(left + right) // 2]

    while pr >= pl:
        while input_list[pl] < pivot:
            pl += 1
        while input_list[pr] > pivot:
            pr -= 1
        if pr >= pl:
            input_list[pl], input_list[pr] = input_list[pr], input_list[pl]
            pl += 1
            pr -= 1

    if pr > left:
        quick_sort(input_list, left, pr)
    if pl < right:
        quick_sort(input_list, pl, right)


if __name__ == '__main__':
    print('셸 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    input_list = [None] * num

    for i in range(num):
        input_list[i] = int(input(f'input_list[{i}]: '))

    quick_sort(input_list, 0, len(input_list) - 1)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'input_list[{i}] = {input_list[i]}')
