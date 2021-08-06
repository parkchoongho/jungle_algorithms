print('+와 -를 번갈아 출력합니다.')
n = int(input('몇개를 출력할까요?: '))

for _ in range(n // 2):
    print('+-', end='')

if n % 2 != 0:
    print("+")

print()