import sys

desk_num = int(sys.stdin.readline().rstrip())

temporary_storage = [0] * 6
max_storage = [0] * 6

for _ in range(desk_num):
    score = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in range(6):
        if i == score[0] or i == score[1]:
            temporary_storage[i] += 1
        else:
            temporary_storage[i] = 0

    for j in range(6):
        if max_storage[j] < temporary_storage[j]:
            max_storage[j] = temporary_storage[j]

max = 0
index = 0
for i in range(6):
    if max < max_storage[i]:
        max = max_storage[i]
        index = i

print(str(max) + " " + str(index))
