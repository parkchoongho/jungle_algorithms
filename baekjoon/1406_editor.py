import sys
from collections import deque

left_stack = deque()
right_stack = deque()

input_string = sys.stdin.readline().rstrip()

for ele in input_string:
    left_stack.append(ele)

input_cnt = int(sys.stdin.readline().rstrip())

for _ in range(input_cnt):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'L':
        if len(left_stack) == 0:
            continue
        else:
            char = left_stack.pop()
            right_stack.append(char)
    elif cmd[0] == 'D':
        if len(right_stack) == 0:
            continue
        else:
            char = right_stack.pop()
            left_stack.append(char)
    elif cmd[0] == 'B':
        if len(left_stack) > 0:
            left_stack.pop()
    else:
        left_stack.append(cmd[1])

str = ''
while len(left_stack) > 0:
    str += left_stack.popleft()

while len(right_stack) > 0:
    str += right_stack.pop()

print(str)
