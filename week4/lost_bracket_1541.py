import sys

expression = sys.stdin.readline().rstrip()

expression_list = expression.split('-')

num_list = []


for val in expression_list:
    num = 0
    str_val = val.split('+')
    for j in str_val:
        num += int(j)
    num_list.append(num)
total = num_list[0]

for i in range(1, len(num_list)):
    total -= num_list[i]

print(total)
