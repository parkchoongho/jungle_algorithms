a = input()
b = input()
str_b = str(b)[::-1]
a = int(a)
sum = 0
for index in range(len(str_b)):
    num = (a * int(str_b[index]))
    print(num)
    sum += num * (10 ** index)
print(sum)
