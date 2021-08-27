import sys

N, K = map(int, sys.stdin.readline().split())

num_list = [0] * N
for i in range(N):
    num_list[i] = int(sys.stdin.readline())


num_list.sort(reverse=True)


coin_count = 0
for val in num_list:
    if K >= val:
        coin_count += K // val
        K %= val


print(coin_count)
