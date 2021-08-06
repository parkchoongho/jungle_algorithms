a = int(input('몇개의 별을 출력하나요?'))
b = int(input('몇개마다 줄을 바꾸나요?'))

line_num = a // b

for _ in range(line_num):
    print('*' * b)
print('*' * (a % b))