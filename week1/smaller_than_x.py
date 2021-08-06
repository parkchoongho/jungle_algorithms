input_list = input().split()

x = int(input_list[1])

num_list = input().split()

result_list = []
for index in range(len(num_list)):
    num = int(num_list[index])
    if num < x:
        result_list.append(str(num))
s = ' '
result = s.join(result_list)
print(result)