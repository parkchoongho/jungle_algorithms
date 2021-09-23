import sys

num_count = sys.stdin.readline()

input_num = sys.stdin.readline().rstrip()

total = 0

for num in input_num:
    total += int(num)

print(total)
