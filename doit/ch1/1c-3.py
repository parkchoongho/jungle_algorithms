print('2자리 양수를 입력하세요.')

while True:
    no = int(input('값을 입력하세요.: '))
    if no >= 10 and no <= 99:
        break
print(f"지금 입력받은 양수는 {no}입니다.")