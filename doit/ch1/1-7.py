print('1부터 n까지 정수 합을 구하세요')

n = int(input('n값을 입력하세요: '))

sum = 0

i = 1

while i <= n:
    sum += i
    i += 1

print(f"1부터 {n}까지 정수 합은 {sum}입니다.")