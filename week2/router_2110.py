import sys

house_num, router_num = map(int, sys.stdin.readline().split())

house_list = [None] * house_num
for i in range(house_num):
    house_list[i] = int(sys.stdin.readline())

house_list.sort()


def install_router(house_list, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = house_list[0]
        count = 1

        for i in range(1, len(house_list)):
            if house_list[i] >= current + mid:
                count += 1
                current = house_list[i]

        if count >= router_num:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


start = 1
end = house_list[-1] - house_list[0]
answer = 0

install_router(house_list, start, end)
print(answer)
