import sys

test_num = int(sys.stdin.readline())


def is_vps(input_string):
    open_stack = []
    for ch in input_string:
        if ch == '(':
            open_stack.append('(')
        else:
            if not open_stack:
                return 'NO'
            else:
                del open_stack[len(open_stack) - 1]
    if not open_stack:
        return 'YES'
    else:
        return 'NO'


for _ in range(test_num):
    print(is_vps(sys.stdin.readline().rstrip()))
