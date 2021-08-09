num = int(input())

post = [0] * num
flag_a = [False] * num
flag_b = [False] * (2 * num - 1)
flag_c = [False] * (2 * num - 1)

def put(num):
    for i in range(num):
        print(f"{post[i]:2}", end='')
    print()

result_list = []
def set(i, num):
    for j in range(num):
        if(not flag_a[j] 
            and not flag_b[i + j] 
            and not flag_c[i - j + (num - 1)]):
            post[i] = j
            if i == (num - 1):
                print(post)
                result_list.append(post)
                put(num)
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (num - 1)] = True
                set(i + 1, num)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + (num - 1)] = False

set(0, num)

print(result_list)