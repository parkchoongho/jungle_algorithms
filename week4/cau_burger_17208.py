import sys

N, M, K = map(int, sys.stdin.readline().split())

order_list = []

for _ in range(N):
    order_list.append(list(map(int, sys.stdin.readline().split())))


record = [[[0] * (K + 1) for _ in range(M + 1)] for _ in range(N + 1)]


for order_index in range((N + 1)):
    for burger_index in range((M + 1)):
        for potato_index in range((K + 1)):
            if order_index == 0 or burger_index == 0 or potato_index == 0:
                record[order_index][burger_index][potato_index] = 0
                continue
            elif burger_index >= order_list[order_index - 1][0] and potato_index >= order_list[order_index - 1][1]:
                record[order_index][burger_index][potato_index] = max(record[order_index - 1][burger_index][potato_index], 1 + record[order_index - 1][burger_index - order_list[order_index - 1][0]][potato_index - order_list[order_index - 1][1]])
                continue
            record[order_index][burger_index][potato_index] = record[order_index - 1][burger_index][potato_index]

print(record[N][M][K])
