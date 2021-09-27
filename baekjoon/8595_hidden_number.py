import sys

string_len = sys.stdin.readline()

hidden_string = sys.stdin.readline()

total = 0

num_str = ''
for i in hidden_string:
    if 48 <= ord(i) <= 57:
        num_str += i
    else:
        if len(num_str) > 0:
            total += int(num_str)
            num_str = ''

print(total)
