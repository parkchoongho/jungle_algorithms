maximum = int(input())
order = 1

for index in range(2, 10):
    num = int(input())
    if num > maximum:
        maximum = num
        order = index

print(maximum)
print(order)