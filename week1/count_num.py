a = int(input())
b = int(input())
c = int(input())

num = a * b * c

num_str = str(num)

for i in range(10):
    num = 0
    for ch in num_str:
        if ch == str(i):
            num += 1
    print(num)