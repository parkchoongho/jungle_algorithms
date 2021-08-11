import sys

height_list = [None] * 9
for i in range(9):
    dwarf_height = int(sys.stdin.readline().rstrip())
    height_list[i] = dwarf_height

height_sum = 0
for height in height_list:
    height_sum += height


def find_spy(height_list):
    for i in range(len(height_list) - 1):
        for j in range(i + 1, len(height_list)):
            if height_list[i] + height_list[j] == height_sum - 100:
                del height_list[j]
                del height_list[i]
                return height_list


dwarf_list = find_spy(height_list)
dwarf_list.sort()
for dwarf in dwarf_list:
    print(dwarf)
