num_count = int(input())

prime_list = [False, False] + [True] * (10000 - 1)

for i in range(2, 10000 + 1):
    if prime_list[i]:
        for j in range(2 * i,  10000 + 1, i):
            prime_list[j] = False

result_list = []
for _ in range(num_count):
    num = int(input())
    for j in range((num//2), num):
        if prime_list[j] and prime_list[num - j]:
            result_list.append(str(num - j) + " " + str(j))
            break

for result in result_list:
    print(result)