test_case_num = int(input())

result_list = []
for i in range(test_case_num):
    input_list = input().split()
    sum = 0
    stu_num = int(input_list[0])

    for i in range(1, len(input_list)):
        sum += int(input_list[i])

    average = sum / stu_num

    ratio_num = 0
    for i in range(1, len(input_list)):
        if average < int(input_list[i]):
            ratio_num += 1
    result_list.append(f"{ratio_num * 100 /stu_num:.3f}%")

for result in result_list:
    print(result)
