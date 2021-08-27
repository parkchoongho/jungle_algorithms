import sys

N = int(sys.stdin.readline())

meetings = []

for _ in range(N):
    meetings.append(list(map(int, sys.stdin.readline().split())))


meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
next_start = 0
for meeting in meetings:
    if meeting[0] >= next_start:
        count += 1
        next_start = meeting[1]

print(count)
