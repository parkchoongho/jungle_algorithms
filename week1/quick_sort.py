def quick_sort(input_list, left, right):
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


num = int(input())
input_list = []

for i in range(num):
    input_list.append(int(input()))


quick_sort(input_list, 0, len(input_list) - 1)

for i in input_list:
    print(i)
