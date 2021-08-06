num_count = int(input())

num_list = input().split()

prime_list = [False, False] + [True] * (1000 - 1)

for i in range(2, 1000 + 1):
    if prime_list[i]:
        for j in range(2 * i,  1000 + 1, i):
            prime_list[j] = False

result_count = 0
for num in num_list:
    if prime_list[int(num)] == True:
        result_count += 1

print(result_count)