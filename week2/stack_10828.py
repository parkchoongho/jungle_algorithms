import sys

test_num = int(sys.stdin.readline())

stack = []


def do_command(command):
    command_list = command.split()
    if command_list[0] == 'push':
        stack.append(int(command_list[1]))
    elif command_list[0] == 'pop':
        if not stack:
            print(-1)
        else:
            value = stack[len(stack) - 1]
            del stack[len(stack) - 1]
            print(value)
    elif command_list[0] == 'size':
        print(len(stack))
    elif command_list[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif command_list[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[len(stack) - 1])


for _ in range(test_num):
    do_command(sys.stdin.readline())
