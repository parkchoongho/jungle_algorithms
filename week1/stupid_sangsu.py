input_list = input().split()

a = int(input_list[0][::-1])
b = int(input_list[1][::-1])

if a > b:
    print(a)
else:
    print(b) 