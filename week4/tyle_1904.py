import sys

n = int(sys.stdin.readline())


def dynamic_programming(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    arr = [1, 1, 2]
    for i in range(3, n + 1):
        if i % 2 == 0:
            arr[2] = arr[1] % 15746 + arr[2] % 15746
        else:
            arr[1] = arr[1] % 15746 + arr[2] % 15746
    if n % 2 == 0:
        return arr[2] % 15746
    else:
        return arr[1] % 15746


print(dynamic_programming(n))
