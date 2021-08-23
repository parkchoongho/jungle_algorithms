import sys
sys.setrecursionlimit(10000)


def dfs(x, y, count):
    global max_count

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    max_count = max(max_count, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and visited[board[nx][ny]] == 0:
            visited[board[nx][ny]] = 1
            dfs(nx, ny, count + 1)
            visited[board[nx][ny]] = 0


R, C = map(int, sys.stdin.readline().split())

board = [list(map(lambda x: ord(x) - 65, sys.stdin.readline().rstrip())) for _ in range(R)]


visited = [0] * 26

visited[board[0][0]] = 1

max_count = 1

dfs(0, 0, max_count)

print(max_count)
