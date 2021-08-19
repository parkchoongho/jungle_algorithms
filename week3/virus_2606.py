import sys

vertex_num = int(sys.stdin.readline())

pair_num = int(sys.stdin.readline())

graph = [[] for _ in range(vertex_num + 1)]

for _ in range(pair_num):
    src, dest = map(int, sys.stdin.readline().split())
    graph[src].append(dest)
    graph[dest].append(src)

visited = [False] * (vertex_num + 1)


def dfs(graph, vertex):
    visited[vertex] = True
    for i in graph[vertex]:
        if not visited[i]:
            dfs(graph, i)


dfs(graph, 1)

print(visited.count(True) - 1)
