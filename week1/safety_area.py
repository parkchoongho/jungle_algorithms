import sys

count_num = int(input())

sys.setrecursionlimit(10000000)
height_info = [None] * count_num
for i in range(count_num):
    height_info[i] = list(map(int, sys.stdin.readline().split()))

is_in_water_list = [[False] * count_num for _ in range(count_num)]


def check_is_in_water(i, j, num):
    if 0 <= i < num and 0 <= j < num:
        if is_in_water_list[i][j] == False:
            is_in_water_list[i][j] = True
            check_is_in_water(i + 1, j, num)
            check_is_in_water(i, j + 1, num)
            check_is_in_water(i - 1, j, num)
            check_is_in_water(i, j - 1, num)
        else:
            return
    return


max_height = 0
for i in range(count_num):
    for j in range(count_num):
        if height_info[i][j] > max_height:
            max_height = height_info[i][j]


max_area_count = 0
for rain in range(0, max_height + 1):

    for i in range(count_num):
        for j in range(count_num):
            if height_info[i][j] <= rain:
                is_in_water_list[i][j] = True
            else:
                is_in_water_list[i][j] = False

    area_count = 0
    for i in range(count_num):
        for j in range(count_num):
            if is_in_water_list[i][j] == True:
                continue
            else:
                area_count += 1
                check_is_in_water(i, j, count_num)
    max_area_count = max(max_area_count, area_count)


print(max_area_count)
