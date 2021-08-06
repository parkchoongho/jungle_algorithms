a, b = map(int, input().split())

cut_count = int(input())

a_list = [a]
b_list = [b]

for _ in range(cut_count):
    x, y = map(int, input().split())
    
    if x == 0:
        sum = 0
        for i in range(len(b_list)):
            sum += b_list[i]
            if sum > y:
                let_in_num2 = sum - y
                let_in_num1 = b_list[i] - let_in_num2
                del b_list[i]
                b_list.insert(i, let_in_num1)
                b_list.insert(i + 1, let_in_num2)
                break
    if x == 1:
        sum = 0
        for i in range(len(a_list)):
            sum += a_list[i]
            if sum > y:
                let_in_num2 = sum - y
                let_in_num1 = a_list[i] - let_in_num2
                del a_list[i]
                a_list.insert(i, let_in_num1)
                a_list.insert(i + 1, let_in_num2)
                break

print(max(a_list) * max(b_list))

        
            