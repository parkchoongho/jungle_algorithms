import sys

test_num = int(sys.stdin.readline())

stack = []

for _ in range(test_num):
    value = int(sys.stdin.readline())
    if value == 0:
        del stack[len(stack) - 1]
    else:
        stack.append(value)

print(sum(stack))
