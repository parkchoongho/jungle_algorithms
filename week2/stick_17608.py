import sys

test_num = int(sys.stdin.readline())

input_list = []

for i in range(test_num):
    input_list.append(int(sys.stdin.readline()))


biggest = input_list[-1]

count = 1
for i in range(len(input_list) - 1, -1, -1):
    if input_list[i] > biggest:
        count += 1
        biggest = input_list[i]

print(count)
