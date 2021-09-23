import sys

input_str = sys.stdin.readline().rstrip()

total = 0
if input_str[0] == '0':
    if input_str[1] == 'x':
        real_num = input_str.split('x')[1]
        digit = len(real_num) - 1
        for i in real_num:
            if i == 'a':
                total += (16 ** digit) * 10
            elif i == 'b':
                total += (16 ** digit) * 11
            elif i == 'c':
                total += (16 ** digit) * 12
            elif i == 'd':
                total += (16 ** digit) * 13
            elif i == 'e':
                total += (16 ** digit) * 14
            elif i == 'f':
                total += (16 ** digit) * 15
            else:
                total += (16 ** digit) * int(i)
            digit -= 1
        print(total)
        exit(0)
    digit = len(input_str) - 2
    for i in range(1, len(input_str)):
        total += (8 ** digit) * int(input_str[i])
        digit -= 1
    print(total)
    exit(0)
else:
    print(int(input_str))
