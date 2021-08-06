num = int(input())

if num < 100:
    print(num)
elif num == 1000:
    print(144)
else:
    result = 99
    for i in range(100, num + 1):
        a = i // 100
        b = (i - a * 100) // 10
        c = i % 10
        if a + c == 2 *b:
            result += 1
    print(result)


