import sys

len_a, len_b = map(int, sys.stdin.readline().split())

list_a = list(map(int, sys.stdin.readline().split()))
list_b = list(map(int, sys.stdin.readline().split()))

sum_array = list_a + list_b

sum_array.sort()

for i in sum_array:
    print(i, end=' ')

print()
