graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def dfs(v: int, visited: list = []):
    visited.append(v)

    for dst in graph[v]:
        if dst not in visited:
            visited = dfs(dst, visited)

    return visited


print(dfs(1))
