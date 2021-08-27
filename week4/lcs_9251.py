import sys

first_string = ' ' + sys.stdin.readline().rstrip()
second_string = ' ' + sys.stdin.readline().rstrip()


lcs = [[0] * len(second_string) for _ in range(len(first_string))]

for i in range(1, len(first_string)):
    for j in range(1, len(second_string)):
        if first_string[i] == second_string[j]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

print(lcs[len(first_string) - 1][len(second_string) - 1])
