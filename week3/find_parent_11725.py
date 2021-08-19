import sys

sys.setrecursionlimit(1000000)

vertex_num = int(sys.stdin.readline())


graph = [[] for _ in range(vertex_num + 1)]

for _ in range(vertex_num - 1):
    src, dest = map(int, sys.stdin.readline().split())
    graph[src].append(dest)
    graph[dest].append(src)


visited = [False] * (vertex_num + 1)
parent = [None] * (vertex_num + 1)


def dfs(graph, vertex):
    visited[vertex] = True
    for i in graph[vertex]:
        if not visited[i]:
            parent[i] = vertex
            dfs(graph, i)


dfs(graph, 1)


for i in range(2, len(parent)):
    print(parent[i])
