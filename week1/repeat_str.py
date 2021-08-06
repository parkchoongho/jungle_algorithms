test_case_num = int(input())

string_list = []
for i  in range(test_case_num):
    input_list = input().split()
    repeat_num = int(input_list[0])
    str_ele = '' 
    for ch in input_list[1]:
        str_ele += ch * repeat_num
    string_list.append(str_ele)
print(string_list)
for i in string_list:
    print(i)
