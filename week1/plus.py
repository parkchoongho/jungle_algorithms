test_case_num = int(input())

result_list = []
for index in range(test_case_num):
    input_list = input().split()
    a = int(input_list[0])
    b = int(input_list[1])
    result_list.append(a + b)

for result in result_list:
    print(result)