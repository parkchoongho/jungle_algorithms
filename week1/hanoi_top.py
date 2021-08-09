num = int(input())

print(2**num-1)

def hanoi(n, a, b):
    if n == 0:
        return

    if n > 1:
        hanoi(n - 1, a, 6 - a - b)
    

    print(f"{a} {b}")

    if n > 1:
         hanoi(n - 1, 6 - a - b, b)


hanoi(num, 1 ,3)