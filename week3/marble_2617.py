import sys

N, M = map(int, sys.stdin.readline().split())

marble_graph_heavier = [[] for _ in range(N + 1)]
marble_graph_lighter = [[] for _ in range(N + 1)]

for _ in range(M):
    heavier, lighter = map(int, sys.stdin.readline().split())
    marble_graph_heavier[heavier].append(lighter)
    marble_graph_lighter[lighter].append(heavier)


def dfs(graph, start_vertex):
    global check
    visited[start_vertex] = True
    for i in graph[start_vertex]:
        if not visited[i]:
            check += 1
            dfs(graph, i)


count = 0

for i in range(1, N + 1):
    visited = [False] * (N + 1)

    check = 0
    dfs(marble_graph_heavier, i)
    if check > N // 2:
        count += 1

    check = 0
    dfs(marble_graph_lighter, i)
    if check > N // 2:
        count += 1

print(count)
