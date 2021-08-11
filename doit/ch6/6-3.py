from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    ccnt = 0
    scnt = 0
    n = len(a)
    for i in range(n - 1):
        print(f'패스 {i + 1}')
        exchange = 0
        for j in range(0, n - i - 1, 1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + (' ' if m != j else ' +' if a[j] > a[j + 1] else ' -'), end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j] > a[j + 1]:
                scnt += 1
                exchange += 1
                a[j + 1], a[j] = a[j], a[j + 1]
        if exchange == 0:
            break
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end=' ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환를 {scnt}번 했습니다.')


if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')