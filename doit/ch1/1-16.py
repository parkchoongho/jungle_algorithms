print('1부터 n까지 정수 합을 구하세요')

while True:
    n = int(input('n값을 입력하세요: '))
    if n > 0:
        break

sum = 0

for i in range(1, n + 1):
    sum += i


print(f"1부터 {n}까지 정수 합은 {sum}입니다.")