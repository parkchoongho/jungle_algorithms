import sys

N, K = map(int, sys.stdin.readline().split())

cargo = []

for _ in range(N):
    cargo.append(list(map(int, sys.stdin.readline().split())))

record = [[0] * (K + 1) for _ in range(N + 1)]

for burden_index in range(N + 1):
    for weight_index in range(K + 1):
        if burden_index == 0 or weight_index == 0:
            record[burden_index][weight_index] = 0
            continue
        if weight_index >= cargo[burden_index - 1][0]:
            record[burden_index][weight_index] = max(record[burden_index - 1][weight_index], cargo[burden_index - 1][1] + record[burden_index - 1][weight_index - cargo[burden_index - 1][0]])
            continue
        record[burden_index][weight_index] = record[burden_index - 1][weight_index]

print(record[N][K])
